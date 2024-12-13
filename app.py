import streamlit as st
from sidebar import add_sidebar  # Correct import

from utils import add_client, load_database

def main():
    st.title("Clinic App")

    # Sidebar for navigation
    add_sidebar()  # This will call the function from sidebar.py

    # Display the corresponding content based on sidebar selection
    if st.session_state["selected_section"] == "Add Client":
        add_client_tab()
    elif st.session_state["selected_section"] == "Client Overview":
        client_overview_tab()

def add_client_tab():
    st.subheader("Add Client")
    name = st.text_input("Client Name")
    age = st.number_input("Age", min_value=0)
    contact = st.text_input("Contact")
    medical_history = st.text_area("Medical History")

    if st.button("Add Client", key="add_client_button"):  # Unique key for the button
        new_entry = {"Name": name, "Age": age, "Contact": contact, "Medical History": medical_history}
        add_client(new_entry)  # Call the add_client function from utils
        st.success("Client Added Successfully!")
        st.balloons()  # Celebrate with balloons!

def client_overview_tab():
    st.subheader("Client Overview")
    data = load_database()  # Load the database to show client data
    st.write(data)

if __name__ == "__main__":
    main()
