import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.title("🏥 MedCare AI")

        st.markdown(
            """
            Your intelligent hospital customer service assistant.

            Ask questions about:

            - 🕒 Visiting hours
            - 📅 Appointments
            - 💳 Billing & Insurance
            - 🏥 Hospital Services
            - 📍 Hospital Policies
            """
        )

        st.divider()

        st.subheader("💡 Example Questions")

        st.markdown("""
- What are your visiting hours?
- Do you accept NHIA insurance?
- Can I book an appointment online?
- Where is the emergency department?
- What specialist clinics do you have?
""")

        st.divider()

        st.subheader("📊 Session Statistics")

        st.metric(
            "Questions Asked",
            st.session_state.questions_asked
        )

        response_time = st.session_state.get("response_time", 0.0)

        if response_time > 0:
            st.metric(
                "Last Response",
                f"{response_time:.2f}s"
            )

        st.divider()

        if st.button(
            "🗑️ Clear Conversation",
            use_container_width=True
        ):
            st.session_state.messages = []
            st.session_state.questions_asked = 0
            st.session_state.last_result = None
            st.session_state.response_time = 0.0

            st.rerun()