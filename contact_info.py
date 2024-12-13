import streamlit as st
import os

def display_contact_info():
    st.subheader("Contact Info")
    
    # Define the correct path to the image
    image_path = os.path.join("denttest", "content", "denta.JPG")
    
    # Try to load and display the image
    try:
        st.image(image_path, width=200)  # Adjust the width if necessary
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        
    # Display other contact information or details here
    st.write("Clinic Address: Example address, City, Country")
    st.write("Phone Number: +123456789")
    st.write("Email: example@clinic.com")
