from openai import OpenAI
import streamlit as st

# Get API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

prompt = 'Hello, how are you?'
completion = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
print(completion.choices[0].message.content)
