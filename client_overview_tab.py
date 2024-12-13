import streamlit as st
import pandas as pd
from utils import load_database

def client_overview_tab():
    st.subheader("Client Overview")
    data = load_database()  # Load the database to show client data
    
    # Apply custom styles to the table
    st.markdown(
        """
        <style>
            .dataframe tbody tr:nth-child(odd) {
                background-color: #f2f2f2;
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
                padding: 10px;
                font-size: 14px;
                border: 1px solid #ddd;
            }
        </style>
        """, unsafe_allow_html=True)

    # Display the data in a styled dataframe
    st.dataframe(data, width=800, height=500)  # Adjust width and height
