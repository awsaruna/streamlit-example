from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai
from gtts import gTTS
import base64

st.markdown("""
    <meta property="og:title" content="TeenTalk" />
    <meta property="og:description" content="Description of your app" />
    <meta property="og:image" content="URL_to_thumbnail_image.png" />
    <meta property="og:url" content="URL_of_your_app" />
<style>
    body {
        background-color: #fffdfa;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    div.main {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    .stApp, .css-145kmo2, .css-17eq0hr, .css-qbe2hs, .css-1aumxhk, .css-17y0c9n, .css-1v3fh75, .css-t8sg0s, .css-1dbjc4n {
        color: #8000ff !important;
    }
    .footer {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 12px;
    }
    
</style>
""", unsafe_allow_html=True)

st.image("https://e2009.s3.us-west-1.amazonaws.com/Untitled+Oct+04.png", width=200)
st.title("TeenTalk - Your life and happiness in your hands! :smile:")
st.write("Made by Karthick Arun")
st.divider()
# Setting the API key
openai.api_key = st.secrets["API_KEY"]

user_input = st.text_input("Your life is very precious, you can make a difference in the world. I am here for you....", placeholder="please type what your concerns here, I am here to help.")
if st.button("Submit", type="primary"):
    #prompt = "Check the sentiment of the following phrase and if its negative then convert it to a positive phrase, start with a very supportive and understanding tone\n\nDesired format:Original Phrase:,Sentiment:,Converted Phrase:\n\nText:'"+user_input+"'"
    prompt = "You are a student councelor with very deep compasion, you are a the trusted adult. Check the sentiment of the following phrase and if its negative then advise the student in an encouraging tone. Start with a very supportive and understanding tone. If any topics of suicide or self harm to others or the user then refer them to the teen suicide help hotline phone or text numeber. Just say the advise and no additional information\n\nText:'"+user_input+"'"
    # Create a chatbot using ChatCompletion.create() function
    completion = openai.ChatCompletion.create(
    # Use GPT 3.5 as the LLM
    model="gpt-3.5-turbo",
    # Pre-define conversation messages for the possible roles
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
      ]
    )
    # Print the returned output from the LLM model
   # print(completion.choices[0].message)
    st.write(completion.choices[0].message["content"])

    tts = gTTS(completion.choices[0].message["content"], lang="en", slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3", format='audio/mp3')
st.markdown("""
**Disclaimer:** This web app is powered by experimental AI technology. It is not a substitute for professional mental health advice or treatment. It is not licensed, nor should it be used for addressing serious mental health issues related to suicide or other severe diagnoses. If you or someone you know is in crisis or needs immediate help, please dial the international crisis helpline at **988** and consult with a trusted adult or mental health professional.
""")

    
# Define the user prompt message
#prompt = "Say the following sentence in a very positive and constructive way, start with a very supportive and understanding tone:'you look ugly and stupid'"
