import streamlit as st

def display_contact_info():
    st.subheader("Contact Information")

    # Display the image in a small rectangle (adjust width and height)
    image_path = "path_to_your_image.jpg"  # Replace with your image path
    st.image(image_path, width=200)  # Adjust the width as needed

    # Add other contact details below
    st.text("For any inquiries, reach us at: example@example.com")
