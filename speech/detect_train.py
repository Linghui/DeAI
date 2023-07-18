import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pandas as pd
from joblib import dump
import os
import random

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

# 提取音频特征
features = []
labels=[]

count = 0

person_dir = "human"

files_in_directory = os.listdir(person_dir)

for file in random.sample(files_in_directory, 500):
    print(file)
    labels.append("human")
    data = extract_features(person_dir+file)
    features.append(data)
    count += 1
    if count > 500:
        break

count = 0
ai_dir = "/home/ipfs10/vicuna/temp/speech/train/"
files_in_directory = os.listdir(ai_dir)
for file in files_in_directory:
    print(file)
    labels.append("ai")
    data = extract_features(ai_dir + file)
    features.append(data)
    if count > 500:
        break


# 假设你有一个音频文件列表 audio_files 和对应的标签列表 labels
# for file in audio_files:
#     data = extract_features(file)
#     features.append(data)

# 将特征和标签转化为 numpy 数组
X = np.array(features)
y = np.array(labels)

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建 SVM 分类器
clf = svm.SVC(kernel='linear')  # 线性核

# 使用训练集训练分类器
clf.fit(X_train, y_train)

# 使用测试集预测
y_pred = clf.predict(X_test)

# 计算精度
print("Accuracy:", accuracy_score(y_test, y_pred))

dump(clf, 'ai_detect.joblib') 

