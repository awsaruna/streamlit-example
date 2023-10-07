from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai
from gtts import gTTS
import base64

st.title("Teen Talk - Your life and happiness in your hands! :sunglasses:")

# Add custom CSS for branding
st.write(
    """
    <style>
    body {
        background-color: #f0f0f0;
        color: #991cff; /* Set text color to hex#991cff (purple) */
        font-family: 'Roboto Mono', monospace; /* Use Roboto Mono font */
    }
    .logo {
        max-width: 200px;
        display: block;
        margin: 20px auto;
    }
    </style>
    """
)

# Add your logo using HTML
st.markdown('<img class="logo" src="https://cac-2023.s3.us-west-1.amazonaws.com/teentalklogo.png" alt="Logo">', unsafe_allow_html=True)

st.divider()

# Setting the API key
openai.api_key = st.secrets["API_KEY"]

user_input = st.text_input("You life is very precious, you can make a difference in the world. I am here for you....", "please type what your concerns here, I am here to help.")

if st.button("Submit", type="primary"):
    #prompt = "Check the sentiment of the following phrase and if its negative then convert it to a positive phrase, start with a very supportive and understanding tone\n\nDesired format:Original Phrase:,Sentiment:,Converted Phrase:\n\nText:'"+user_input+"'"
    prompt = "You are a student councelor. Check the sentiment of the following phrase and if its negative then advise the student in an encouraging tone. Start with a very supportive and understanding tone. Just say the advise and no additional information\n\nText:'"+user_input+"'"
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
    
# Define the user prompt message
#prompt = "Say the following sentence in a very positive and constructive way, start with a very supportive and understanding tone:'you look ugly and stupid'"
