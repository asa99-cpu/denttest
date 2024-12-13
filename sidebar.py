import streamlit as st

def add_sidebar():
    """Create a sidebar for navigation."""
    st.sidebar.title("Navigation")
    
    # Use session_state to store the selected tab
    selected_section = st.sidebar.radio(
        "Select Section",
        ("Add Client", "Client Overview"),
        key="selected_section_radio"
    )
    
    # Save the selection to session_state to access in the main app
    st.session_state["selected_section"] = selected_section
