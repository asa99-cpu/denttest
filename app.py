import streamlit as st
from utils import load_database, add_client_tab, client_overview_tab
from sidebar import add_sidebar
import start  # Import the start.py file

def main():
    """Main function to run the app."""
    
    # Check if user has visited before, else show the start page
    if "selected_section" not in st.session_state:
        st.session_state["selected_section"] = "Start Page"

    if st.session_state["selected_section"] == "Start Page":
        # Show the welcome animation page
        start.display_welcome_animation()
    else:
        # Show the sidebar and sections after the user clicks "Enter Clinic App"
        add_sidebar()
        # Show the content based on selected section
        if st.session_state["selected_section"] == "Add Client":
            add_client_tab()
        elif st.session_state["selected_section"] == "Client Overview":
            client_overview_tab()
        elif st.session_state["selected_section"] == "Contact Info":
            st.write("Contact Info Placeholder")

if __name__ == "__main__":
    main()
