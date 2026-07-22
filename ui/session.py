import streamlit as st

from ui.resources import get_chatbot


def initialize_session():
    """
    Initialize Streamlit session state.
    """

    # Conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chatbot instance
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = get_chatbot()

    # Chat statistics
    if "questions_asked" not in st.session_state:
        st.session_state.questions_asked = 0

    # Feedback storage
    if "feedback" not in st.session_state:
        st.session_state.feedback = {}

    # Last chatbot response
    if "last_result" not in st.session_state:
        st.session_state.last_result = None

    # Response time
    if "response_time" not in st.session_state:
        st.session_state.response_time = 0.0

    # Pending suggested question
    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None