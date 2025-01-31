import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.title('Chatting App')

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to display chat
def display_chat():
    for chat in st.session_state.chat_history:
        st.write(f"{chat['timestamp']} - {chat['user']}: {chat['message']}")

# User input
user_input = st.text_input("Enter your message")

# Button to send message
if st.button('Send'):
    if user_input:
        st.session_state.chat_history.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user': 'User',  # You can also add a user authentication system
            'message': user_input
        })
        user_input = ''  # Clear input box

# Display chat history
display_chat()
