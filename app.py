import streamlit as st
from sidebar import add_sidebar
from utils import add_client_tab, client_overview_tab, display_contact_info

# Initialize session state for selected_section if it does not exist
if "selected_section" not in st.session_state:
    st.session_state["selected_section"] = "Add Client"  # Default section

def main():
    # Sidebar navigation
    add_sidebar()

    # Display the correct section based on the selected section
    selected_section = st.session_state["selected_section"]
    
    if selected_section == "Add Client":
        add_client_tab()
    elif selected_section == "Client Overview":
        client_overview_tab()
    elif selected_section == "Contact Info":
        display_contact_info()

if __name__ == "__main__":
    main()
