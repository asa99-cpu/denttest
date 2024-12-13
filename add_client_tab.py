import streamlit as st
from utils import add_client

def add_client_tab():
    st.subheader("Add Client")

    # Create a form for adding a client
    with st.form(key="add_client_form"):
        # Inputs for client details
        name = st.text_input("Client Name")
        age = st.number_input("Age", min_value=0, help="Enter the client's age")
        contact = st.text_input("Contact", help="Enter the client's phone number or email")
        medical_history = st.text_area("Medical History", help="Enter any medical history details")

        # Add a submit button with a custom label
        submit_button = st.form_submit_button("Add Client")

    # When the form is submitted
    if submit_button:
        # Ensure that required fields are filled
        if not name or not contact:
            st.error("Client name and contact information are required!")
        elif age <= 0:
            st.error("Please enter a valid age.")
        else:
            # If validation passes, create a new client entry
            new_entry = {"Name": name, "Age": age, "Contact": contact, "Medical History": medical_history}
            add_client(new_entry)  # Call the add_client function from utils
            st.success("Client added successfully!")
            st.balloons()  # Celebrate with balloons!

            # Optionally, reset form fields
            st.experimental_rerun()  # Reload to show updated client list
