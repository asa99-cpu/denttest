import streamlit as st
from sidebar import add_sidebar  # Correct import
from utils import add_client, load_database
from contact_info import display_contact_info  # Import the function for contact info
import time

# Create the landing page with animation and reklams
def landing_page():
    # Display a catchy title and background color
    st.markdown("""
    <div style="background-color:#FFDDC1; padding:20px;">
        <h1 style="text-align:center; color:#FF6347;">Welcome to کلینیکی شادیار!</h1>
        <p style="text-align:center; font-size:20px; color:#8B0000;">We are here to provide the best dental care for you!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Adding a simple animation with CSS
    st.markdown("""
    <div style="text-align:center;">
        <h2 style="color:#FF6347;">💥 Our Services Will Blow Your Mind! 💥</h2>
        <p style="font-size:18px; color:#6A5ACD;">Stay tuned for the best dental care experience you will ever have.</p>
        <div style="width:100%; height:5px; background-color:#FF6347; animation: slide 2s ease-out infinite;"></div>
    </div>

    <style>
        @keyframes slide {
            0% { width: 0%; }
            100% { width: 100%; }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Display an image (optional, you can replace it with any image URL)
    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <img src="https://www.w3schools.com/html/img_girl.jpg" alt="Clinic Image" width="300"/>
    </div>
    """, unsafe_allow_html=True)
    
    # Add a countdown or delay before moving to the main page
    st.write("You will be redirected to our clinic information shortly...")
    time.sleep(5)  # Delay for 5 seconds
    
    # Set the flag in session state to hide the landing page and show the main content
    st.session_state['show_landing'] = False

# Main function to handle different pages
def main():
    # Initialize session state variable if not already set
    if 'show_landing' not in st.session_state:
        st.session_state['show_landing'] = True

    # Show the landing page first, and then show the sidebar and content
    if st.session_state['show_landing']:
        landing_page() 
    else:
        # Sidebar for navigation
        add_sidebar()  # This will call the function from sidebar.py

        # Display the corresponding content based on sidebar selection
        if st.session_state["selected_section"] == "Add Client":
            add_client_tab()
        elif st.session_state["selected_section"] == "Client Overview":
            client_overview_tab()
        elif st.session_state["selected_section"] == "Contact Info":
            display_contact_info()  # Show the contact info tab

def add_client_tab():
    st.subheader("Add Client")
    name = st.text_input("Client Name")
    age = st.number_input("Age", min_value=0)
    contact = st.text_input("Contact")
    medical_history = st.text_area("Medical History")

    if st.button("Add Client", key="add_client_button"):  # Unique key for the button
        new_entry = {"Name": name, "Age": age, "Contact": contact, "Medical History": medical_history}
        add_client(new_entry)  # Call the add_client function from utils
        st.success("Client Added Successfully!")
        st.balloons()  # Celebrate with balloons!

def client_overview_tab():
    st.subheader("Client Overview")
    data = load_database()  # Load the database to show client data
    st.write(data)

if __name__ == "__main__":
    main()
