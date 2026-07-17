import streamlit as st

from ui.styles import load_css
from ui.session import initialize_session
from ui.header import render_header
from ui.sidebar import render_sidebar
from ui.suggestions import render_suggestions
from ui.chat import render_chat


st.set_page_config(
    page_title="MedCare AI Assistant",
    page_icon="🏥",
    layout="wide",
)


def main():
    load_css()

    initialize_session()

    render_header()

    render_sidebar()

    render_suggestions()

    render_chat()


if __name__ == "__main__":
    main()