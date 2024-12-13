# utils.py

import pandas as pd
import os
import requests
import streamlit as st
import base64
import io

def load_database():
    """Load the database from GitHub or fallback to local CSV."""
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            content = base64.b64decode(response.json()["content"]).decode("utf-8")
            data = pd.read_csv(io.StringIO(content))
        else:
            if os.path.exists(LOCAL_DATABASE_FILE):
                data = pd.read_csv(LOCAL_DATABASE_FILE)
            else:
                data = pd.DataFrame(columns=["Name", "Age", "Contact", "Medical History"])
        return data
    except Exception as e:
        st.error(f"Error loading database: {e}")
        return pd.DataFrame(columns=["Name", "Age", "Contact", "Medical History"])

def add_client_tab():
    """Function for the 'Add Client' tab in the app"""
    st.subheader("Add Client")
    name = st.text_input("Client Name")
    age = st.number_input("Age", min_value=0)
    contact = st.text_input("Contact")
    medical_history = st.text_area("Medical History")

    if st.button("Add Client", key="add_client_button"):
        new_entry = {"Name": name, "Age": age, "Contact": contact, "Medical History": medical_history}
        add_client(new_entry)
        st.success("Client Added Successfully!")
        st.balloons()

def client_overview_tab():
    """Function for the 'Client Overview' tab in the app"""
    st.subheader("Client Overview")
    data = load_database()  # Load the database to show client data
    st.write(data)
