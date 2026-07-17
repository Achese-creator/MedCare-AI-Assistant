import streamlit as st

from ui.sources import render_sources

def render_chat():
    """
    Render the chatbot conversation.
    """

    # Display previous messages
    for message in st.session_state.messages:

        avatar = "👤" if message["role"] == "user" else "🏥"

        with st.chat_message(
            message["role"],
            avatar=avatar,
        ):
            st.markdown(message["content"])

    typed_prompt = st.chat_input(
    "Ask a question about the hospital..."
)

    prompt = typed_prompt

    if st.session_state.pending_prompt:
        prompt = st.session_state.pending_prompt
        st.session_state.pending_prompt = None

    if prompt:

        # Display user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant", avatar="🏥"):

            with st.spinner("Searching hospital knowledge..."):

                result = st.session_state.chatbot.ask(prompt)
                
            st.session_state.last_result = result
            st.session_state.response_time = result["response_time"]
            st.session_state.questions_asked += 1    

            st.markdown(result["answer"])

            col1, col2 = st.columns([3, 1])

            with col2:
                st.caption(
                    f"⚡ {result['response_time']:.2f}s"
                )
            render_sources()

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result["answer"],
            }
        )

        # Save metadata
        st.session_state.last_result = result
        st.session_state.response_time = result["response_time"]
        st.session_state.questions_asked += 1