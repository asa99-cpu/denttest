import streamlit as st
from utils import load_database

def client_overview_tab():
    st.subheader("Client Overview")
    
    # Load the database to show client data
    data = load_database()  

    if not data.empty:
        # Styling the table to make it look nicer
        st.dataframe(data, use_container_width=True)  # Display the table with container width

        # Optionally, you can add more styling such as adjusting the font size or color
        st.markdown("""
            <style>
                .stDataFrame {
                    font-size: 14px;
                    font-family: 'Arial';
                }
                .stDataFrame table {
                    width: 100%;
                    border-collapse: collapse;
                }
                .stDataFrame th, .stDataFrame td {
                    padding: 12px;
                    text-align: left;
                    border: 1px solid #ddd;
                }
                .stDataFrame th {
                    background-color: #f2f2f2;
                    color: #333;
                }
                .stDataFrame tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                .stDataFrame tr:hover {
                    background-color: #f1f1f1;
                }
            </style>
        """, unsafe_allow_html=True)  # Add custom CSS for the table styling
    else:
        st.write("No client data available.")
