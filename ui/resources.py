import streamlit as st

from chatbot.rag_chain import RAGChatbot
from chatbot.retrieval import get_retriever


@st.cache_resource
def get_chatbot() -> RAGChatbot:
    """
    Create and cache the chatbot instance.
    """

    retriever = get_retriever()

    return RAGChatbot(retriever)