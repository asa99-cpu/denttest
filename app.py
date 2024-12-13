import streamlit as st
from utils import add_client_tab, client_overview_tab
from sidebar import add_sidebar
from contact_info import display_contact_info

def main():
    st.title("Clinic App")

    # Add sidebar for navigation
    add_sidebar()

    # Check the selected section from session state
    if "selected_section" not in st.session_state:
        st.session_state["selected_section"] = "Add Client"  # Default section

    if st.session_state["selected_section"] == "Add Client":
        add_client_tab()
    elif st.session_state["selected_section"] == "Client Overview":
        client_overview_tab()
    elif st.session_state["selected_section"] == "Contact Info":
        display_contact_info()

if __name__ == "__main__":
    main()
