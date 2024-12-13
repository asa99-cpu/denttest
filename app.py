import streamlit as st
from utils import add_client, load_database
from sidebar import render_sidebar  # Import the sidebar rendering function

def main():
    st.title("Clinic App")

    # Add the sidebar
    selected_option = render_sidebar()  # Get the selected option from the sidebar

    # Check for the selected option and route accordingly
    if selected_option == "Add Client":
        add_client_tab()
    elif selected_option == "Client Overview":
        client_overview_tab()
    elif selected_option == "Welcome" or selected_option is None:
        st.write("Welcome to the Clinic App!")

def add_client_tab():
    st.subheader("Add Client")
    name = st.text_input("Client Name")
    age = st.number_input("Age", min_value=0)
    contact = st.text_input("Contact")
    medical_history = st.text_area("Medical History")

    if st.button("Add Client"):
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
