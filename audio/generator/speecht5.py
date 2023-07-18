from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset
import random
import nltk
import os

# 读取文件
with open('../art/en.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 将文章按照句子分割
sentences = nltk.sent_tokenize(text)

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")



# load xvector containing speaker's voice characteristics from a dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")


# if there is no ../ai/speecht5 directory then create it
if not os.path.exists("../ai/speecht5"):
    os.makedirs("../ai/speecht5")


count = 0
for i in range(1, 101):
    random_number = random.randint(1, 7000) # embeddings_dataset has arround 7000 samples
    speaker_embeddings = torch.tensor(embeddings_dataset[random_number]["xvector"]).unsqueeze(0)

    # 生成一个随机数（在1到3之间）
    num_sentences = random.randint(1, 3)
    chosen_sentences = random.sample(sentences, num_sentences)
    joined_str = ''.join(chosen_sentences)
    print(joined_str)

    inputs = processor(text=joined_str.strip(), return_tensors="pt")
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    
    sf.write("../ai/speecht5/ai_voice_"+str(count)+".wav", speech.numpy(), samplerate=16000)
    count += 1

