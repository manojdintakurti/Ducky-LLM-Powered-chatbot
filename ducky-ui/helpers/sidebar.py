import streamlit as st

def show() -> None:

    with st.sidebar:
        st.markdown(f"""
            <a href="/" style="color:black;text-decoration: none;">
                <div style="display:table;margin-top:-1rem;margin-left:0%;">
                    <span style="font-size: 1.5em; font-weight: bold;">🐥 Ducky</span>
                    <span style="font-size: 0.8em; color: grey">&nbsp;&nbsp;v0.1.0</span>
                    <br>
                    <span style="font-size: 0.8em">Your AI-powered coding assistant!</span>
                </div>
            </a>
            <br>
        """, unsafe_allow_html=True)

        reload_button = st.button("↪︎  Reload Page")
        if reload_button:
            st.session_state.clear()
            st.rerun()