import streamlit as st
import helpers.sidebar
from helpers.logo import add_logo


st.set_page_config(
    page_title="Ducky",
    page_icon="🐥",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.image("ducky.png", width=150)  # Adjust width as needed

helpers.sidebar.show()

st.write("# Welcome to Ducky!")
st.write("Your Intelligent Coding Companion for Debugging, Reviewing, and Code Generation")

st.markdown("""
### What can Ducky do for you?
- 💡 Get instant answers to your programming questions.
- 📘 Learn and explore topics across different programming languages.
- 🧐 Review your code and receive detailed, constructive feedback.
- 🛠️ Identify and fix bugs in your code with clear explanations.
- ✏️ Assist in editing and improving your code as per your requirements.

Get started by selecting an option from the sidebar!
""")

st.markdown("---")

st.markdown("""
### How to use Ducky:
- **Quick Chat**: Get immediate, concise answers to any programming-related queries.
- **Learn** Programming: Choose a topic and receive detailed, personalized explanations.
- **Code Review**: Upload your code for in-depth analysis and improvement recommendations.
- **Debug Code**: Share your code and errors to receive troubleshooting and debugging assistance.
- **Modify Code**: Submit your code with specific changes in mind for tailored modification support.


Choose the task you need help with from the sidebar and follow the prompts on each page.
""")

st.markdown("---")

st.markdown("""
💡 **Tips for getting the most out of Ducky**:
- Be specific in your questions and descriptions for more accurate assistance.
- For code-related tasks, provide as much context as possible.
- Don't hesitate to ask for clarifications or further explanations.
- Use the conversation history feature in code modification for iterative improvements.
- Always review and understand the code and explanations provided before using them in your projects.
""")

st.markdown("---")
st.markdown("Keep in mind, Ducky is here to guide and support your learning journey. While it offers helpful insights, building your own understanding and coding skills is key. Happy coding!")