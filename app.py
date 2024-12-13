import streamlit as st
from sidebar import add_sidebar
from add_client import add_client_tab
from contact_info import display_contact_info

def main():
    # Check if the "selected_section" exists in session_state, if not, initialize it
    if "selected_section" not in st.session_state:
        st.session_state["selected_section"] = "Add Client"  # Set default value to "Add Client"
    
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
