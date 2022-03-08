# import packages
from pytube import YouTube
import os

# url input from user
yt = YouTube(str(input("Enter your url: ")))

# extract only audio/mp4
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
# put (/) before home so that it goes to the right folder
print("enter destination or leave blank for current directory")
destination = str(input(">> ")) or "."

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

# result of success
print(yt.title + " " + "has been successfully downloaded ")

