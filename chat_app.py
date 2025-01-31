import streamlit as st
import random
from transformers import pipeline

# Initialize the AI model
model = pipeline("text-generation", model="gpt2")

st.set_page_config(page_title="Cartoon Chat App", page_icon=":robot:")

st.markdown(
    """
    <style>
    body {
        background-color: #f0e6f6;
    }
    .title {
        font-size: 48px;
        color: #ff6347;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .chat-box {
        background-color: #fffacd;
        border: 2px solid #ff6347;
        padding: 10px;
        border-radius: 10px;
    }
    .input-box {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">Cartoon Chat App</div>', unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def display_chat():
    for chat in st.session_state.chat_history:
        st.markdown(
            f'<div class="chat-box"><strong>{chat["user"]}:</strong> {chat["message"]}</div>',
            unsafe_allow_html=True
        )

user_input = st.text_input("Enter your message", key="input_box", help="Type your message here!")

if st.button('Send', key="send_button"):
    if user_input:
        st.session_state.chat_history.append({
            'user': 'You',
            'message': user_input
        })
        # Generate a response from the AI model
        ai_response = model(user_input, max_length=50, num_return_sequences=1)
        st.session_state.chat_history.append({
            'user': 'AI',
            'message': ai_response[0]['generated_text']
        })
        st.experimental_rerun()

display_chat()
