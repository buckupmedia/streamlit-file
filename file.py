import streamlit as st
import pandas as pd


st.subheader("Uploading the CSV File and Displaying it ")
df  = st.file_uploader("upload the file ", type = ['csv', 'xlsx'])
if df is not None:
    data = pd.read_csv(df)
    st.dataframe(data.head(10))

st.subheader("Displaying the backend Data Directly ")
df1 = pd.read_csv(r"C:\Users\hp\Downloads\geeks for geeks\streamlit\Products.csv")
if df1 is not None:
    st.table(df1.head(10))





st.subheader("Uploading the Image File and Displaying it ")
img = st.file_uploader("Upload the image ", type = ["jpeg", "png"])
if img is not None:
    st.image(img)

st.subheader("Displaying the Image  Directly ")
st.image(r"C:\Users\hp\Downloads\geeks for geeks\streamlit\img.png")





st.subheader("Uploading the video File and Displaying it ")
video_file= st.file_uploader("Upload the file : ", type= ["mp4"])
if video_file is not None:
    st.video(video_file, start_time  = 1)

st.subheader("[Playing the Video  Directly ")
st.video(r"C:\Users\hp\Downloads\geeks for geeks\streamlit\video.mp4")





st.subheader("Uploading the audio File and playing it ")
audio_file= st.file_uploader("Upload the file : ", type= ["mp3"])
if audio_file is not None:
    st.audio(audio_file.read())

st.subheader("[Playing the Audio  Directly ")
st.audio(r"C:\Users\hp\Downloads\geeks for geeks\streamlit\song.mp3", start_time = 40)
