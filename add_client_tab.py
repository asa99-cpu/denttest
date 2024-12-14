import streamlit as st
from utils import add_client

def add_client_tab():
    st.subheader("Add Client")

    # Create a form for adding a client
    with st.form(key="add_client_form"):
        # Input for client name (still text input as before)
        name = st.text_input("Client Name")

        # Dropdown for selecting age (10 to 60 years)
        age = st.selectbox("Age", options=list(range(10, 61)))  # Dropdown from 10 to 60

        # Input for contact information (still text input)
        contact = st.text_input("Contact", help="Enter the client's phone number or email")

        # Text area for medical history (still text area)
        medical_history = st.text_area("Medical History", help="Enter any medical history details")

        # Add a submit button with a custom label
        submit_button = st.form_submit_button("Add Client")

    # When the form is submitted
    if submit_button:
        # Ensure that required fields are filled
        if not name or not contact:
            st.error("Client name and contact information are required!")
        else:
            # If validation passes, create a new client entry
            new_entry = {"Name": name, "Age": age, "Contact": contact, "Medical History": medical_history}
            add_client(new_entry)  # Call the add_client function from utils
            st.success("Client added successfully!")
            st.balloons()  # Celebrate with balloons!

            # Optionally, reset form fields
            st.experimental_rerun()  # Reload to show updated client list
