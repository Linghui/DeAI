import concurrent.futures
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset
import random
import nltk


# 并行声音生成测试，结果不理想 效率没有提高
# 读取文件
with open('art.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 将文章按照句子分割
sentences = nltk.sent_tokenize(text)

model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")


def task(n):
    print(f"Processing {n} start")
    random_number = random.randint(1, 7000)
    speaker_embeddings = torch.tensor(embeddings_dataset[random_number]["xvector"]).unsqueeze(0)

    # 生成一个随机数（在1到3之间）
    num_sentences = random.randint(1, 3)
    chosen_sentences = random.sample(sentences, num_sentences)
    joined_str = ''.join(chosen_sentences)
    print(joined_str)

    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")

    inputs = processor(text=joined_str.strip(), return_tensors="pt")
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    
    sf.write("output/ai_voice_"+str(n)+".wav", speech.numpy(), samplerate=16000)
    print(f"Processing {n} end")

# load xvector containing speaker's voice characteristics from a dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    tasks = {executor.submit(task, i) for i in range(1, 11)}

    # 等待所有任务完成
    for future in concurrent.futures.as_completed(tasks):
        # 你可以在这里处理每个任务的结果（如果有的话）
        pass


