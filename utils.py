# utils.py

import os
import requests
import pandas as pd
import base64
import io
import streamlit as st

# Configuration Variables
LOCAL_DATABASE_FILE = "Database.csv"
GITHUB_REPO = "asa99-cpu/denttest"  # Replace with your actual GitHub repository name
GITHUB_FILE_PATH = "Database.csv"   # The path to your database file in GitHub
GITHUB_TOKEN = st.secrets["github"]["token"]  # Ensure that you have the GitHub token saved in Streamlit secrets

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
