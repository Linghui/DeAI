import numpy as np
import librosa
from joblib import load
import os

# for testing
# 加载保存的分类器
clf = load('ai_detect.joblib') 

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

person_dir = "/home/ipfs10/vicuna/temp/download/zh-CN_test_0/"
# file = path + "common_voice_zh-CN_18982914.mp3"

# person_dir = "./output/"
cout = 0
files_in_directory = os.listdir(person_dir)
for file in files_in_directory:
    X = extract_features(person_dir+file)
    Xs = [X]

    # 使用加载的分类器进行预测
    predictions = clf.predict(Xs)

    print(predictions)
    cout += 1
    if cout > 50:
        break
