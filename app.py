import streamlit as st
from utils import add_client, load_database

def main():
    st.title("Clinic App")

    # Add Client Tab
    add_client_tab()

    # Client Overview Tab
    client_overview_tab()

def add_client_tab():
    st.subheader("Add Client")
    name = st.text_input("Client Name")
    age = st.number_input("Age", min_value=0)
    contact = st.text_input("Contact")
    medical_history = st.text_area("Medical History")

    if st.button("Add Client"):
        new_entry = {"Name": name, "Age": age, "Contact": contact, "Medical History": medical_history}
        add_client(new_entry)
        st.success("Client Added Successfully!")

def client_overview_tab():
    st.subheader("Client Overview")
    data = load_database()
    st.write(data)

if __name__ == "__main__":
    main()

