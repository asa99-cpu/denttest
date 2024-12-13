import streamlit as st
from sidebar import add_sidebar
from add_client import add_client_tab
from contact_info import display_contact_info

def main():
    # Set the initial state of the selected section
    if "selected_section" not in st.session_state:
        st.session_state["selected_section"] = "Add Client"  # Default section

    # Add sidebar with navigation
    add_sidebar()

    # Show the appropriate content based on the selected section
    selected_section = st.session_state["selected_section"]

    if selected_section == "Add Client":
        add_client_tab()
    elif selected_section == "Client Overview":
        # You can add the client overview functionality here
        st.subheader("Client Overview")
        st.write("Client overview content will go here.")
    elif selected_section == "Contact Info":
        display_contact_info()

if __name__ == "__main__":
    main()
