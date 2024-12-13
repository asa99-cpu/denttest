import streamlit as st
import pandas as pd
from utils import load_database

def client_overview_tab():
    st.subheader("Client Overview")
    data = load_database()  # Load the database to show client data

    # Style the DataFrame for better presentation
    st.markdown(
        """
        <style>
            .dataframe tbody tr:nth-child(odd) {
                background-color: #f9f9f9;
            }
            .dataframe tbody tr:nth-child(even) {
                background-color: #ffffff;
            }
            .dataframe th {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
            .dataframe td {
                padding: 8px;
            }
        </style>
        """, unsafe_allow_html=True)

    # Display the DataFrame with Streamlit's enhanced features
    st.dataframe(data, width=800, height=500)  # Adjust width and height for better visibility
