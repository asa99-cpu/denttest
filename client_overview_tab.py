import streamlit as st
import pandas as pd
from utils import load_database

def client_overview_tab():
    st.subheader("Client Overview")
    data = load_database()  # Load the database to show client data
    
    if not data.empty:
        # Display the table with better styling
        st.dataframe(data.style.set_properties(**{
            'background-color': 'lightblue', 
            'color': 'black'
        }).set_table_styles(
            [{'selector': 'thead th', 'props': [('background-color', 'darkblue'), ('color', 'white')]}]
        ).hide_index())
    else:
        st.write("No client data available.")
