import os
import streamlit as st

def display_contact_info():
    st.subheader("Contact Info")
    
    # Print the current working directory to verify
    st.write("Current Working Directory:", os.getcwd())
    
    # Define the correct path to the image
    image_path = os.path.join("denttest", "content", "denta.JPG")
    
    # Try to load and display the image
    try:
        st.image(image_path, width=200)  # Adjust the width if necessary
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
