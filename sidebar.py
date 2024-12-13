import streamlit as st

def render_sidebar():
    """Render the sidebar with buttons for navigation and return the selected option."""
    with st.sidebar:
        st.title("Navigation")

        # Initialize session state for the selected page if not already done
        if "selected_page" not in st.session_state:
            st.session_state.selected_page = "Welcome"  # Default page

        # Buttons for navigation
        if st.button("Welcome"):
            st.session_state.selected_page = "Welcome"
        if st.button("Add Client"):
            st.session_state.selected_page = "Add Client"
        if st.button("Client Overview"):
            st.session_state.selected_page = "Client Overview"

    return st.session_state.selected_page  # Return the selected page from session state
