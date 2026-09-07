import os
import streamlit as st


def render_sources():
    """
    Display the sources used to generate the last response.
    """

    result = st.session_state.last_result

    if not result or not result.get("success", False):
        return

    sources = result.get("sources", [])

    if not sources:
        return

    with st.expander("Sources Used"):

        st.caption(
            "This answer was generated from the following hospital knowledge base documents:"
        )

        for source in sources:
            filename = os.path.basename(source)

            st.success(f"{filename}")

        st.info(
            "The assistant answers only from indexed hospital documents and will state when information is unavailable."
        )