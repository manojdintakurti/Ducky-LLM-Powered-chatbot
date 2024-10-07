import streamlit as st
from services import prompts
from helpers import util

st.set_page_config(
    page_title="Quick Code Chat",
    page_icon="⚙️",
    layout="wide"
)

import helpers.sidebar
import asyncio

helpers.sidebar.show()

st.header("Quick Code Chat")
st.write("Get instant answers to your coding questions and quick code snippets.")

# Ensure the session state is initialized
if "messages" not in st.session_state:
    initial_messages = [{"role": "system",
                         "content": prompts.quick_chat_system_prompt()}]
    st.session_state.messages = initial_messages

# Print all messages in the session state
for message in [m for m in st.session_state.messages if m["role"] != "system"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat with the LLM, and update the messages list with the response.
# Handles the chat UI and partial responses along the way.
async def chat(messages):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        messages = await util.run_conversation(messages, message_placeholder)
        st.session_state.messages = messages
    return messages


# React to the user prompt
if prompt := st.chat_input("Ask a coding question or request a code snippet..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    asyncio.run(chat(st.session_state.messages))

# Add some example questions to help users get started
st.sidebar.markdown("## Example Questions")
st.sidebar.markdown("""
- How do I reverse a list in Python using slicing?
- What’s the difference between __init__ and __new__ in Python classes?
- Can you show me how to create a simple POST request in Flask?
- How do I work with context managers in Python?
- What are some tips for optimizing Python code for performance?
""")