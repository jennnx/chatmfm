import os
import whisper
from tqdm import tqdm
import time

model = whisper.load_model("medium.en")

audio_dir = "./audio_files"
audio_files = [file_name for file_name in os.listdir(audio_dir) if file_name.endswith(".mp4")]

start_time = time.time()
for i, file_name in enumerate(tqdm(audio_files)):
    audio_path = os.path.join(audio_dir, file_name)
    result = model.transcribe(audio_path)

    # Save transcription to file with same name as audio file
    transcription_path = os.path.join("./transcriptions", os.path.splitext(file_name)[0] + ".txt")
    with open(transcription_path, 'w') as f:
        f.write(result["text"])

    # Print progress indicators
    if i % 10 == 0:
        elapsed_time = time.time() - start_time
        time_per_file = elapsed_time / (i + 1)
        time_left = time_per_file * (len(audio_files) - (i + 1))
        tqdm.write(f"Processed {i+1}/{len(audio_files)} files, elapsed time: {elapsed_time:.2f}s, time left: {time_left:.2f}s")

elapsed_time = time.time() - start_time
tqdm.write(f"Finished processing {len(audio_files)} files in {elapsed_time:.2f}s")
