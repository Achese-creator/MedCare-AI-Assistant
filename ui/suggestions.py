import streamlit as st


SUGGESTED_QUESTIONS = [
    "🕒 What are your visiting hours?",
    "📅 How can I book an appointment?",
    "💳 Do you accept NHIA insurance?",
    "🏥 What specialist services do you offer?",
]


def render_suggestions():
    """
    Display suggested questions before the conversation starts.
    """

    # Only show suggestions before any messages have been sent
    if st.session_state.messages:
        return

    st.markdown("### 💡 Try asking...")

    cols = st.columns(2)

    for i, question in enumerate(SUGGESTED_QUESTIONS):
        with cols[i % 2]:
            if st.button(question, use_container_width=True):
                # Store the selected suggestion so chat.py can process it
                st.session_state.pending_prompt = question[2:].strip()
                st.rerun()