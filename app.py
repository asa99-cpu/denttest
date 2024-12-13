import streamlit as st
from utils import add_client, load_database
from sidebar import add_sidebar

def main():
    st.title("Clinic App")

    # Sidebar with navigation
    add_sidebar()

    # Check which page to display based on the sidebar selection
    if st.session_state.get('current_page') == "Add Client":
        add_client_tab()
    elif st.session_state.get('current_page') == "Client Overview":
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
    # Initialize the session state for tracking the current page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Add Client"  # Default page is Add Client
    main()
