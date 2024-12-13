# utils.py
import requests
import pandas as pd
import base64
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "your-username"  # Replace with your GitHub username
REPO_NAME = "denttest"        # Replace with your repository name
FILE_PATH = "Database.csv"
BRANCH_NAME = "main"

def load_database():
    """Fetch the file from GitHub and load it into a DataFrame."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}?ref={BRANCH_NAME}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_content = response.json()
        file_data = base64.b64decode(file_content['content']).decode('utf-8')
        return pd.read_csv(pd.compat.StringIO(file_data))
    else:
        raise Exception(f"Failed to fetch file from GitHub. Status code: {response.status_code}")

def add_client(new_entry):
    """Add a new client entry to the database."""
    data = load_database()
    new_data = data.append(new_entry, ignore_index=True)
    save_database(new_data)

def save_database(data):
    """Save the DataFrame to GitHub."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    # Convert DataFrame to CSV
    csv_content = data.to_csv(index=False)

    # Encode the content in base64
    encoded_content = base64.b64encode(csv_content.encode('utf-8')).decode('utf-8')

    payload = {
        "message": "Update Database.csv",
        "content": encoded_content,
        "branch": BRANCH_NAME
    }

    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Database updated successfully!")
    else:
        raise Exception(f"Failed to update database on GitHub. Status code: {response.status_code}")
