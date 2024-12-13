import os
import streamlit as st

def display_contact_info():
    st.subheader("Contact Info")
    
    # Define the correct relative path to the image
    image_path = os.path.join("content", "denta.JPG")
    
    # Check if the image exists before displaying
    if os.path.exists(image_path):
        st.image(image_path, width=200)  # Adjust the width if necessary
    else:
        st.error(f"Image not found at {image_path}")
