import os
import streamlit as st

def display_contact_info():
    # Set the page title with right alignment using markdown
    st.markdown('<h1 style="text-align: right;">پەیوەندی کردن</h1>', unsafe_allow_html=True)
    
    # Define the correct relative path to the image
    image_path = os.path.join("content", "denta.JPG")
    
    # Check if the image exists before displaying
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)  # Use 'use_container_width' instead of 'use_column_width'
    else:
        st.error(f"Image not found at {image_path}")

    # Section introduction with a welcoming message
    st.markdown("## Welcome to our Dental Clinic!")
    st.write("We are here to provide you with the best dental care. Feel free to reach out for any inquiries or appointments.")

    # Add contact details with icons for visual enhancement
    st.markdown("### Contact Details")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("📞")
    with col2:
        st.write("**Phone Number:** ٠٧٥٠٣٢٢٣٩٥٦")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("✉️")
    with col2:
        st.write("**Email:** clinic@example.com")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("🏠")
    with col2:
        st.write("**Address:** 123 Clinic St, City, Country")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("🌐")
    with col2:
        st.write("**Social Media:** [Facebook](https://facebook.com/clinic) | [Instagram](https://instagram.com/clinic) | [Twitter](https://twitter.com/clinic)")

    # Contact form
    st.markdown("### Contact Us")
    st.write("Feel free to leave a message for any questions or to book an appointment!")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success("Your message has been sent successfully!")
            # Here, you can add functionality to send the message to your email or store it in the database.

    # Add a back-to-home button to improve navigation
    st.markdown("---")
    if st.button("Back to Home"):
        st.session_state["selected_section"] = "Add Client"
