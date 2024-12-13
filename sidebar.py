import streamlit as st

def render_sidebar():
    """Render the sidebar with buttons for navigation and return the selected option."""
    with st.sidebar:
        st.title("Navigation")

        # Buttons for navigation
        if st.button("Welcome"):
            return "Welcome"
        if st.button("Add Client"):
            return "Add Client"
        if st.button("Client Overview"):
            return "Client Overview"

    return None  # Default return if no button is clicked
