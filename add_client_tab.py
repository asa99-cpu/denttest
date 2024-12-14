import streamlit as st
from utils import add_client

def add_client_tab():
    st.subheader("Add Client")

    # Create a form for adding a client
    with st.form(key="add_client_form"):
        # Dropdown for selecting client name (Example names)
        name = st.selectbox(
            "Client Name",
            options=["John Doe", "Jane Smith", "Michael Johnson", "Add New..."],  # Example names
            help="Select a client name or choose 'Add New...' to enter a custom name."
        )

        # Dropdown for age group (Example ranges)
        age = st.selectbox(
            "Age Group",
            options=["0-10", "11-20", "21-30", "31-40", "41+"],
            help="Select the client's age group."
        )

        # Dropdown for contact methods
        contact = st.selectbox(
            "Preferred Contact Method",
            options=["Phone", "Email", "WhatsApp", "Other"],
            help="Select the client's preferred contact method."
        )

        # Multi-select for medical history (Example options)
        medical_history = st.multiselect(
            "Medical History",
            options=["No Issues", "Diabetes", "High Blood Pressure", "Allergies", "Asthma"],
            help="Select all medical conditions that apply."
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
                "Medical History": ", ".join(medical_history)  # Combine multiple selections
            }
            add_client(new_entry)  # Call the add_client function from utils
            st.success("Client added successfully!")
            st.balloons()  # Celebrate with balloons!

            # Optionally, reset form fields
            st.experimental_rerun()  # Reload to show updated client list
