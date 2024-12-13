import pandas as pd
import os
import requests
import base64
import streamlit as st

# Path to the local CSV file
DATABASE_FILE = "Database.csv"

# GitHub repository and token details
REPO_OWNER = "your-github-username"  # Replace with your GitHub username
REPO_NAME = "your-repository-name"   # Replace with your GitHub repository name
FILE_PATH = "Database.csv"           # The file path in the repository
BRANCH_NAME = "main"                 # The branch to update

# Load GitHub token from Streamlit secrets
GITHUB_TOKEN = st.secrets["github"]["token"]

def load_database():
    """Load the database from the local CSV file."""
    if os.path.exists(DATABASE_FILE):
        data = pd.read_csv(DATABASE_FILE)
    else:
        # Create an empty DataFrame with the proper columns if the file doesn't exist
        data = pd.DataFrame(columns=["Name", "Age", "Contact", "Medical History"])
    return data

def add_client(new_entry):
    """Add a new client to the database."""
    data = load_database()  # Load existing data

    # Ensure data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(columns=["Name", "Age", "Contact", "Medical History"])

    # Append the new entry to the DataFrame
    data = data.append(new_entry, ignore_index=True)  # Add the new entry at the last row

    # Save the updated DataFrame back to the CSV locally
    data.to_csv(DATABASE_FILE, index=False)

    # Upload the updated CSV to GitHub
    upload_to_github(data)

def upload_to_github(data):
    """Upload the updated database to GitHub."""
    # Convert the DataFrame to CSV and encode it as base64
    csv_data = data.to_csv(index=False)
    encoded_csv = base64.b64encode(csv_data.encode()).decode()

    # GitHub API URL for file updates
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"

    # Get the current file information to retrieve the sha (if the file exists)
    response = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    if response.status_code == 200:
        file_info = response.json()
        sha = file_info['sha']
    else:
        sha = None  # File doesn't exist, no sha needed

    # Data to update the file on GitHub
    data = {
        "message": "Update database.csv",
        "content": encoded_csv,
        "branch": BRANCH_NAME
    }

    if sha:
        data["sha"] = sha  # Include sha for file update if the file exists

    # Send a PUT request to update the file
    response = requests.put(url, json=data, headers={"Authorization": f"token {GITHUB_TOKEN}"})

    if response.status_code == 201:
        print("File uploaded successfully!")
    else:
        print(f"Failed to upload the file to GitHub. Status code: {response.status_code}")
        print(response.text)
