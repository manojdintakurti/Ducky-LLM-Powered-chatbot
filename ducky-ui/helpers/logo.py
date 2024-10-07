import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(ducky.png);
                background-repeat: no-repeat;
                background-position: 20px 20px;
                top:-60px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Ducky";
                margin-left: 20px;
                font-size: 30px;
                position: relative;
                top:-60px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )