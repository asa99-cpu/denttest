import pandas as pd
import os
import requests
import streamlit as st
import base64

# Path to the local CSV file (fallback if GitHub is unavailable)
LOCAL_DATABASE_FILE = "Database.csv"

# Load GitHub token from Streamlit secrets
GITHUB_TOKEN = st.secrets["github"]["token"]
GITHUB_REPO = "your-username/your-repository"  # Replace with your GitHub repo
GITHUB_FILE_PATH = "Database.csv"  # Path to the file in the repository

def load_database():
    """Load the database from GitHub or fallback to local CSV."""
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Decode the content
            content = base64.b64decode(response.json()["content"]).decode("utf-8")
            data = pd.read_csv(pd.compat.StringIO(content))
        else:
            # If GitHub fetch fails, fallback to local file
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
        # Load existing data
        data = load_database()

        # Append the new entry
        data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)

        # Convert the updated DataFrame to CSV
        csv_data = data.to_csv(index=False)

        # Encode the CSV data to base64
        encoded_csv = base64.b64encode(csv_data.encode("utf-8")).decode("utf-8")

        # Fetch the file's SHA (required to update the file on GitHub)
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            sha = response.json()["sha"]
        else:
            # If the file doesn't exist, SHA is not needed for creation
            sha = None

        # Prepare the request payload
        payload = {
            "message": "Add new client entry",
            "content": encoded_csv,
        }
        if sha:
            payload["sha"] = sha

        # Update the file on GitHub
        response = requests.put(url, headers=headers, json=payload)

        if response.status_code in [200, 201]:
            st.success("Client added successfully to GitHub database!")
        else:
            st.error(f"Failed to update GitHub database: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"Error adding client: {e}")
