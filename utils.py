import pandas as pd
import os

# Path to the local CSV file
DATABASE_FILE = "Database.csv"

def load_database():
    """Load the database from the local CSV file."""
    if os.path.exists(DATABASE_FILE):
        return pd.read_csv(DATABASE_FILE)
    else:
        # Return an empty DataFrame if the file doesn't exist
        return pd.DataFrame(columns=["Name", "Age", "Contact", "Medical History"])

def add_client(new_entry):
    """Add a new client to the database."""
    data = load_database()  # Load existing data

    # Ensure data is a DataFrame, in case it's None or something else
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(columns=["Name", "Age", "Contact", "Medical History"])

    # Append the new entry to the DataFrame
    data = data.append(new_entry, ignore_index=True)  # Add the new entry

    # Save the updated DataFrame back to the CSV
    data.to_csv(DATABASE_FILE, index=False)
