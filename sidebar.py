import streamlit as st

def add_sidebar():
    st.sidebar.title("Clinic App")

    # Buttons for each tab
    add_client_button = st.sidebar.button("Add Client")
    client_overview_button = st.sidebar.button("Client Overview")
    contact_info_button = st.sidebar.button("Contact Info")  # New button for contact info
    
    # Show corresponding tab based on the button pressed
    if add_client_button:
        from app import add_client_tab
        add_client_tab()  # Call add_client_tab function

    if client_overview_button:
        from app import client_overview_tab
        client_overview_tab()  # Call client_overview_tab function
    
    if contact_info_button:
        from contact_info import contact_info  # Import the contact_info function
        contact_info()  # Display contact info
