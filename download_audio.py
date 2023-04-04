# Whisper Documentation: https://pypi.org/project/openai-whisper/

# Pytube docs: https://pytube.io/en/latest/

# Tutorial Guide on Transcription via Python: https://dev.to/zirkelc/automatically-transcribe-youtube-videos-with-openai-whisper-1856

from pytube import YouTube
from clean_title import get_episode_number
import time
import json

sample_video_url = 'https://www.youtube.com/watch?v=jMgBdn4Sad8'

def download(url, title):
  yt = YouTube(url)
  audio_stream = yt.streams.filter(only_audio=True).first()
  formatted_title = get_episode_number(title) + ".mp4"
  audio_stream.download(output_path="./audio_files", filename=formatted_title)

if __name__ == '__main__':
  with open('./video_urls/urls.json', 'r') as f:
    videos = json.load(f)

  total_videos = len(videos)
  start_time = time.time()
  for i, video in enumerate(videos, start=1):
    download(video['url'], video['title'])
    minutes_passed = round((time.time() - start_time) / 60, 2)
    print(f"Downloaded video {i}/{total_videos}: {video['title']}. {total_videos - i} videos remaining. {minutes_passed} minutes passed.")
