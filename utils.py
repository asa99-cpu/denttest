import pandas as pd
import os

# Path to the local CSV file
DATABASE_FILE = "Database.csv"

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
    data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)

    # Save the updated DataFrame back to the CSV
    data.to_csv(DATABASE_FILE, index=False)
