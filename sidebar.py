import streamlit as st

def add_sidebar():
    """Create a sidebar with navigation buttons."""
    st.sidebar.title("Navigation")
    
    # List of pages for navigation
    pages = ["Add Client", "Client Overview"]
    
    # Sidebar radio button to select the page
    page_selection = st.sidebar.radio("Select Page", pages)
    
    # Set the current page in session state to track navigation
    st.session_state.current_page = page_selection
