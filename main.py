import whisper

model = whisper.load_model("medium.en")
result = model.transcribe("./audio_files/Asking_A_100M_Year_Founder_For_Profitable_Business_Ideas_413_.mp4")

with open('./transcriptions/business_ideas.txt', 'w') as f:
    f.write(result["text"])