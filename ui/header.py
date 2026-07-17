import streamlit as st


def render_header():
    """
    Render the application header.
    """

    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg,#1f4e79,#2e86c1);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 25px;
            color: white;
            text-align: center;
        ">

        <h1 style="
            margin-bottom:5px;
            color:white;
        ">
            🏥 MedCare AI Assistant
        </h1>

        <p style="
            font-size:18px;
            margin-bottom:0;
            color:#f5f5f5;
        ">
            Intelligent Hospital Customer Support powered by
            <b>Retrieval-Augmented Generation (RAG)</b>
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )