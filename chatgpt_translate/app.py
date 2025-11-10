import os
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key="")

st.title("번역")
sentence = st.text_area("번역하고 싶은 문장", "")
before_sentence = st.selectbox("번역 전 문장", ["영어", "한국어"])
after_sentence = st.selectbox("번역 후 문장", ["영어", "한국어"], index = 1)

def translate_sentence(sentence, before_sentence, after_sentence):
    prompt = f"Translate the following sentence from {before_sentence} to {after_sentence}:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": sentence}
        ]
    )

    translated_text = response.choices[0].message.content
    return translated_text

if st.button("번역"):
    translated_sentence = translate_sentence(sentence, before_sentence, after_sentence)
    st.success(translated_sentence)
