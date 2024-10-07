import streamlit as st
import asyncio
import helpers.sidebar
import services.prompts
import services.llm

st.set_page_config(
    page_title="Ducky Code Assistant",
    page_icon="🦆",
    layout="wide"
)

helpers.sidebar.show()

st.header("Ducky Code Assistant")
st.write("Review, debug, and modify your code with AI assistance.")

# Session state initialization
if 'code' not in st.session_state:
    st.session_state.code = ""
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Function to reset the page
def reset_page():
    st.session_state.code = ""
    st.session_state.conversation_history = []
    st.rerun()

# Code input
st.session_state.code = st.text_area("Enter your code here:", value=st.session_state.code, height=300)

# Action selection
action = st.selectbox("Select an action:", ["Review Code", "Debug Code", "Modify Code"])

async def stream_llm_response(messages):
    response_placeholder = st.empty()
    full_response = ""
    async for content in services.llm.converse(messages):
        if content.startswith("EXCEPTION") or content.startswith("oaiEXCEPTION"):
            st.error(f"An error occurred: {content}")
            return
        full_response += content
        response_placeholder.markdown(full_response + "▌")
    response_placeholder.markdown(full_response)
    return full_response

if action == "Review Code":
    if st.button("Review Code"):
        review_prompt = services.prompts.review_prompt(st.session_state.code)
        messages = services.llm.create_conversation_starter(services.prompts.general_code_assistant_prompt())
        messages.append({"role": "user", "content": review_prompt})
        
        st.markdown("### Code Review")
        asyncio.run(stream_llm_response(messages))

elif action == "Debug Code":
    error_string = st.text_area("Enter error message (if any):")
    if st.button("Debug Code"):
        debug_prompt = services.prompts.debug_prompt(st.session_state.code, error_string)
        messages = services.llm.create_conversation_starter(services.prompts.general_code_assistant_prompt())
        messages.append({"role": "user", "content": debug_prompt})
        
        st.markdown("### Debugging Help")
        asyncio.run(stream_llm_response(messages))

elif action == "Modify Code":
    modification_instructions = st.text_area("Enter modification instructions:")
    if st.button("Modify Code"):
        modify_prompt = services.prompts.modify_code_prompt(st.session_state.code, modification_instructions)
        messages = services.llm.create_conversation_starter(services.prompts.general_code_assistant_prompt())
        messages.append({"role": "user", "content": modify_prompt})
        
        st.markdown("### Modified Code and Explanation")
        full_response = asyncio.run(stream_llm_response(messages))
        if full_response:
            # Update the code in session state with the modified version
            modified_code = full_response.split("```")[1] if "```" in full_response else full_response
            st.session_state.code = modified_code
    
    # Display conversation history
    st.markdown("### Conversation History")
    for i, message in enumerate(st.session_state.conversation_history):
        st.text(f"Message {i+1}: {message}")
    
    # Allow further modifications
    new_modification = st.text_input("Enter new modification request:")
    if st.button("Apply New Modification"):
        st.session_state.conversation_history.append(new_modification)
        # Here you would call the LLM again with the new modification request
        # For brevity, I'm not implementing the full logic here

# Reset button
if st.sidebar.button("Reset Page"):
    reset_page()

# Display the current code
if st.session_state.code:
    st.markdown("### Current Code")
    st.code(st.session_state.code)