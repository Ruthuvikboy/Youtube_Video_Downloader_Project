## The code is designed to download youtube videos
from pytube import YouTube
##pytube is a very old library and may face alot of issues make sure u run
## pip install pytube
## execute this in terminal before excuting code
def Download(link):
    ## This function is used to get the link and download it at the highest resolution
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution()
    youtube_video.download()
    print("YouTube video downloaded")

## Inputing the YouTube video link
link = input("Enter YouTube video link: ")
## Calling the Download Function
Download(link)
