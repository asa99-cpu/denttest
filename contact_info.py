import streamlit as st

def display_contact_info():
    st.subheader("Contact Information")

    # Display the image in a small rectangle (adjust width and height)
    image_path = "path_to_your_image.jpg"  # Replace with the correct path to your image
    st.image(image_path, width=200)  # Adjust the width as needed

    # Add other contact details below the image
    st.markdown("For any inquiries, reach us at: [example@example.com](mailto:example@example.com)")
    st.text("Or call us at: +1-234-567-8901")
    st.text("Our address is: 123 Clinic Street, City, Country")
