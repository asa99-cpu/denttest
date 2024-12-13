import streamlit as st
import os

def display_contact_info():
    st.subheader("Contact Info")
    
    # Set the correct path to the image
    image_path = os.path.join("denttest", "content", "denta.JPG")
    
    # Try to get the absolute path to verify it
    abs_image_path = os.path.abspath(image_path)
    st.write(f"Looking for image at: {abs_image_path}")
    
    try:
        st.image(image_path, width=200)  # Display the image with a width of 200
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        
    # Add other contact information or details here
    st.write("Clinic Address: Example address, City, Country")
    st.write("Phone Number: +123456789")
    st.write("Email: example@clinic.com")
