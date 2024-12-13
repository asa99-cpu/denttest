import streamlit as st
from sidebar import add_sidebar
from utils import add_client, load_database
from add_client_tab import add_client_tab
from client_overview_tab import client_overview_tab

# Main function to control the flow
def main():
    # Initialize session state for page selection if not already initialized
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Add Client"  # Default page

    # Add sidebar with navigation
    add_sidebar()

    # Render the page based on the selection from the sidebar
    if st.session_state.current_page == "Add Client":
        add_client_tab()  # Show Add Client Tab
    elif st.session_state.current_page == "Client Overview":
        client_overview_tab()  # Show Client Overview Tab

# Call main function to run the app
if __name__ == "__main__":
    main()
