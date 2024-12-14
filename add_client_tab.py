import streamlit as st
from utils import add_client

def add_client_tab():
    st.subheader("Add Client")

    # Create a form for adding a client
    with st.form(key="add_client_form"):
        # Inputs for client details
        name = st.text_input("Client Name")

        # Dropdown for age (example: 1-100)
        age = st.selectbox("Age", options=range(1, 101), help="Select the client's age")

        # Dropdown for contact type
        contact_type = st.selectbox("Contact Type", options=["Phone", "Email"], help="Select the type of contact")
        contact = st.text_input(f"Enter {contact_type}", help=f"Enter the client's {contact_type.lower()}")

        # Dropdown for medical history categories
        medical_history_options = [
            "None",
            "Allergy",
            "Diabetes",
            "Hypertension",
            "Heart Disease",
            "Other"
        ]
        medical_history = st.selectbox(
            "Medical History",
            options=medical_history_options,
            help="Select the client's medical history (if any)"
        )

        # Add a submit button with a custom label
        submit_button = st.form_submit_button("Add Client")

    # When the form is submitted
    if submit_button:
        # Ensure that required fields are filled
        if not name or not contact:
            st.error("Client name and contact information are required!")
        else:
            # If validation passes, create a new client entry
            new_entry = {
                "Name": name,
                "Age": age,
                "Contact": contact,
                "Medical History": medical_history
            }
            add_client(new_entry)  # Call the add_client function from utils
            st.success("Client added successfully!")
            st.balloons()  # Celebrate with balloons!

            # Optionally, reset form fields
            st.experimental_rerun()  # Reload to show updated client list
