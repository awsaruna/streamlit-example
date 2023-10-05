from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai

"""
# Teen Talk
You life is very precious, you can make a difference in the world. I am here for you =)
"""
# Setting the API key
openai.api_key = st.secrets["API_KEY"]

user_input = st.text_input("What bothers you?", "say what bothers you")
if st.button("Help!", type="primary"):
    prompt = "Check the sentiment of the following phrase and if its negative then convert it to a positive phrase, start with a very supportive and understanding tone\n\nDesired format:\nOriginal Phrase:\nSentiment:\nConverted Phrase:\n\nText:'"+user_input+"'"
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
    print(completion.choices[0].message)
    st.write(completion.choices[0].message)
    
# Define the user prompt message
#prompt = "Say the following sentence in a very positive and constructive way, start with a very supportive and understanding tone:'you look ugly and stupid'"
