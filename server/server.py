from typing import Union
import numpy as np
import librosa
from joblib import load
import os
from PIL import Image
import sqlite3

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

def extract_features(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None 
    
    # print(mfccsscaled)
    return mfccsscaled

clf = load('../ai_detect.joblib') 

app = FastAPI()

templates = Jinja2Templates(directory="")

@app.on_event("startup")
async def startup():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    with open(f"{file.filename}", "wb") as f:
        f.write(contents)
    
    X = extract_features(file.filename)
    Xs = [X]

    # 使用加载的分类器进行预测
    predictions = clf.predict(Xs)

    # print(predictions)

    return {"filename": file.filename, "prediction": predictions[0]}

@app.post("/uploadimage/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()

    with open(f"{file.filename}", "wb") as f:
        f.write(contents)
    
    image = Image.open(file.filename)
    image = image.convert("RGB")
    image.save(f"processed_{file.filename}")

    return {"filename": file.filename, "message": "Image uploaded successfully"}

@app.get("/cat_canvas", response_class=HTMLResponse)
async def get_cat_canvas(request: Request):
    return templates.TemplateResponse("cat_canvas.html", {"request": request})

@app.post("/submit_score/")
async def submit_score(score: int):
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO scores (score) VALUES (?)', (score,))
    conn.commit()
    conn.close()
    return {"message": "Score submitted successfully"}
