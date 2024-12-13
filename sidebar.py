import streamlit as st

def render_sidebar():
    """Render the sidebar and return the selected option."""
    with st.sidebar:
        st.title("Navigation")
        selected_option = st.radio(
            "Choose a section:",
            options=["Welcome", "Add Client", "Client Overview"],
        )
    return selected_option
