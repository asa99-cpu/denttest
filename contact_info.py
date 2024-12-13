import streamlit as st
import os

def contact_info():
    st.subheader("Contact Information")

    # Display photo (ensure the file path is correct)
    photo_path = "denttest/content/photo.txt"  # Path to the photo file
    try:
        with open(photo_path, "r") as file:
            photo_name = file.read().strip()  # Read the photo name (e.g., "denta")
        
        # Display the photo (assuming the photo is an image file, e.g., "denta.png")
        image_path = f"denttest/content/{photo_name}.png"  # Update file extension if needed
        if os.path.exists(image_path):
            st.image(image_path, caption="Dental Clinic", use_column_width=True)
        else:
            st.warning("Photo not found.")
    except FileNotFoundError:
        st.error("Photo file not found!")

    # Add other contact details
    st.write("For inquiries, please contact:")
    st.write("📧 Email: clinic@example.com")
    st.write("📞 Phone: +1 (123) 456-7890")
    st.write("🌐 Website: www.dentalclinic.com")
