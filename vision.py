from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st
import os 
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to Gemini pro model and get responses

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_responses(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


#Initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input = st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

#If submit is clicked
if submit:
    response = get_gemini_responses(input,image)
    st.subheader("The Response is :")
    st.write(response)