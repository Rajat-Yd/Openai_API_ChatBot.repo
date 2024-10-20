import os
import json
import streamlit as st
import openai
import os

working_dire = os.getcwd()
config_file = json.load(open(f"{working_dire}/config.json"))

OPENAI_API_KEY = config_file["OPENAI_API_KEY"]
openai_api_key = OPENAI_API_KEY

st.set_page_config(
    page_title="CHATBOT",
    page_icon=":robot:🤖",
    layout="centered"
)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.title("🤖 ChatGpt 3.4 Turbo_ChatBot")

for message in st.session_state.get("chat_history",[]):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask GPT Model")

if user_input:
    st.session_state.chat_history.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are a helpful assistant."},
            *st.session_state.get("chat_history",[])
            ]
        )
    bot_response = response["choices"][0]["message"]["content"]
    st.session_state.chat_history.append({"role":"assistant","content":bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

