import streamlit as st
## working media files(video/images/audio)
st.title("Media_Files")


## display images
from PIL import Image
img =Image.open("panda.jpg")
st.image(img,use_column_width =True)

## display videos
video_file = open("sos.mp4","rb").read()
st.video(video_file)

# working with audio file
audio_file =open("song.mp3","rb")
st.audio(audio_file.read())