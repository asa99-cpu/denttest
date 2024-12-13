import streamlit as st

def add_sidebar():
    """Create a sidebar for navigation with buttons."""
    st.sidebar.title("Navigation")
    
    # Add buttons for navigation
    if st.sidebar.button("Add Client"):
        st.session_state["selected_section"] = "Add Client"
    
    if st.sidebar.button("Client Overview"):
        st.session_state["selected_section"] = "Client Overview"
        
    if st.sidebar.button("Contact Info"):
        st.session_state["selected_section"] = "Contact Info"
