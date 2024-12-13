import streamlit as st
from utils import load_database

def client_overview_tab():
    st.subheader("Client Overview")
    data = load_database()  # Load the database to show client data
    st.write(data)
