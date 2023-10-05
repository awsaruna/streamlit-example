from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
# Setting the API key
openai.api_key = st.secrets["API_KEY"]

# Define the user prompt message
#prompt = "Say the following sentence in a very positive and constructive way, start with a very supportive and understanding tone:'you look ugly and stupid'"

prompt = "Check the sentiment of the following phrase and if its negative then convert it to a positive phrase\n\nDesired format:\nOriginal Phrase:\nSentiment:\nConverted Phrase:\n\nText:'you look ugly and stupid'"

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

with st.echo(code_location='below'):
    total_points = st.slider("This is Mr. Lucky", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
