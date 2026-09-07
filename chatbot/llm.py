import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from chatbot.logger import logger

load_dotenv()


class LLMClient:
    """
    Wrapper around the Groq client.
    """

    def __init__(self):

        # Try Streamlit Secrets first
        api_key = st.secrets.get("GROQ_API_KEY")

        # Fallback to local .env
        if not api_key:
            api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            logger.error("GROQ_API_KEY not found.")
            raise ValueError(
                "GROQ_API_KEY not found. Add it to Streamlit Secrets or your local .env file."
            )

        try:
            self.client = Groq(api_key=api_key)
            logger.info("Groq client initialized successfully.")

        except Exception as e:
            logger.exception("Failed to initialize Groq client.")
            raise RuntimeError("Could not initialize the Groq client.") from e

    def get_client(self):
        """
        Return the initialized Groq client.
        """
        return self.client


def get_llm():
    """
    Return a Groq client instance.
    """
    return LLMClient().get_client()