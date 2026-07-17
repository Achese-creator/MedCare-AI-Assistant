import streamlit as st


def load_css():
    """
    Apply custom styling to the application.
    """

    st.markdown(
        """
        <style>

        .main {
            padding-top: 1rem;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        h1 {
            color: #1f4e79;
            font-weight: 700;
        }

        h2, h3 {
            color: #2f5d8c;
        }

        .stChatMessage {
            border-radius: 12px;
            padding: 0.5rem;
        }

        .stButton > button {
            width: 100%;
            border-radius: 8px;
        }

        footer {
            visibility: hidden;
        }

        #MainMenu {
            visibility: hidden;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )