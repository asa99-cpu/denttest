import pandas as pd
import os
import requests
import streamlit as st
import base64
import io

LOCAL_DATABASE_FILE = "Database.csv"
GITHUB_TOKEN = st.secrets["github"]["token"]
GITHUB_REPO = "asa99-cpu/denttest"  
GITHUB_FILE_PATH = "Database.csv"  

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

def add_client(new_entry):
    """Add a new client to the database on GitHub."""
    try:
        data = load_database()
        data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
        csv_data = data.to_csv(index=False)
        encoded_csv = base64.b64encode(csv_data.encode("utf-8")).decode("utf-8")
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.get(url, headers=headers)

        sha = response.json().get("sha", None)
        payload = {
            "message": "Add new client entry",
            "content": encoded_csv,
        }
        if sha:
            payload["sha"] = sha

        response = requests.put(url, headers=headers, json=payload)
        if response.status_code in [200, 201]:
            st.success("Client added successfully to GitHub database!")
        else:
            st.error(f"Failed to update GitHub database: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error adding client: {e}")
