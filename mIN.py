from pytube import YouTube
url = 'https://www.youtube.com/watch?v=rmpQjLPLmdw'
video = YouTube(url)
print(video.title)
print(video.views)
print(video.thumbnail_url)
dw = video.streams.get_audio_only().download()

