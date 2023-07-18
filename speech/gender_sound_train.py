import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pandas as pd
from joblib import dump

# for test a fine tune model, not for production

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
# audio_files=[
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_28.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_8.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_23_48.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_28.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_8.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_23_48.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_28.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_8.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_23_48.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_28.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_22_8.mp3",
#     "/home/ipfs10/vicuna/huggingsound/download/ttsMP3.com_VoiceText_2023-6-15_11_23_48.mp3",
#     ]
labels=[]

df = pd.read_csv('/home/ipfs10/vicuna/temp/download/train.tsv', sep='\t')

count = 0

for index, line in df.iterrows():
    # print("Path: ", line['path'])
    print("Gender: ", line['gender'])
    labels.append(line['gender'])
    data = extract_features("/home/ipfs10/vicuna/temp/download/zh-CN_train_0/" + line['path'])
    features.append(data)
    count += 1
    print("Count: ", count)
    # if count > 2000:
    #     break

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

dump(clf, 'gender_detect.joblib') 

