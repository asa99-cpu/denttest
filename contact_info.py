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
    
    # Display a brief introduction
    st.write("Feel free to reach out to us for any inquiries or appointments.")
    
    # Contact details
    st.write("### Phone Number: +1234567890")
    st.write("### Email: clinic@example.com")
    st.write("### Address: 123 Clinic St, City, Country")
    st.write("### Social Media: [Facebook](https://facebook.com/clinic) | [Instagram](https://instagram.com/clinic) | [Twitter](https://twitter.com/clinic)")

    # Additional tools for user engagement
    st.write("### Contact Us Form")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.success("Your message has been sent successfully!")
            # Here you can integrate functionality to send the message to your email or save it.
    
    # Add a back to home button
    if st.button("Back to Home"):
        st.session_state["selected_section"] = "Add Client"
