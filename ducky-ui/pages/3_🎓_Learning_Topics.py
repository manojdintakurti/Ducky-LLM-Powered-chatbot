import asyncio

import streamlit as st
import helpers.sidebar
import helpers.util
import services.prompts
import services.llm

st.set_page_config(
    page_title="Coding Topics",
    page_icon="🖥️",
    layout="wide"
)

st.header("Coding Topics")

helpers.sidebar.show()

# Add a sidebar option to select a learner level
learner_level = st.sidebar.selectbox("I'd like my answer as if I were a:",
                                     ["beginner programmer", "intermediate programmer", "advanced programmer"])

response_format = st.sidebar.selectbox("I'd like my answer as a:",
                                       ["set of bullet point notes", "tutorial", "code examples", "project idea"])

st.markdown("<br>", unsafe_allow_html=True)

topic = st.text_input("What coding topic would you like to learn about?", placeholder="Ask about a programming concept, language, or technology here.")
answer_button = st.button("Get Answer", type="primary")

if answer_button:
    advice = st.markdown("### Ducky is thinking...")
    learning_prompt = services.prompts.learning_prompt(learner_level, response_format, topic)
    messages = services.llm.create_conversation_starter(services.prompts.system_learning_prompt())
    messages.append({"role": "user", "content": learning_prompt})
    asyncio.run(helpers.util.run_conversation(messages, advice))

# Add some example topics to help users get started
st.sidebar.markdown("## Example Topics")
st.sidebar.markdown("""
- Functional programming in Python
- WebSockets and real-time communication in JavaScript
- Building microservices with Flask or Spring Boot
- Introduction to deep learning and neural networks
""")