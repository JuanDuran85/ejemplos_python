'''
Working with pytube and whisper library to download a video, convert it to audio format and next to convert it to text

'''

import pytube
import whisper

youtube_url: str = "https://www.youtube.com/watch?v=5s7iazAi_18"
youtube_video: pytube.YouTube = pytube.YouTube(youtube_url)

audio: pytube.Stream = youtube_video.streams.get_audio_only()  # type: ignore
audio.download(filename="tem.mp4") 

model = whisper.load_model("small")
result = model.transcribe('tem.mp4')

print(result['text'])