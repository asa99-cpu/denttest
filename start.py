import streamlit as st

def display_welcome_animation():
    """Display animation or attractive page."""
    st.title("Welcome to the Dental Clinic App")

    # Add some dentist-related animations and styles
    st.markdown("""
    <style>
        .welcome-text {
            font-size: 2em;
            text-align: center;
            color: #FF6347;
            animation: fadeIn 3s ease-in-out;
        }

        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }

        .dentist-emoji {
            font-size: 3em;
            animation: bounce 1s infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .button {
            font-size: 1.2em;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #45a049;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display text in Kurdish (Sorani)
    st.markdown("""
    <div class="welcome-text">
        <h1>بەخێربێن بۆ کلینیکی شادیار</h1>
        <p>بەرەو تەبدروستیەکی باشترو سیمایەکی جوانتری ددانەکانمان</p>
    </div>
    <div class="dentist-emoji">🦷</div>
    """, unsafe_allow_html=True)

    # Initialize session state for navigation if not already initialized
    if "selected_section" not in st.session_state:
        st.session_state["selected_section"] = "Welcome"

    # Display "Enter Clinic" button
    if st.button("کرتە لێرە بکە", key="enter_button"):
        st.session_state["selected_section"] = "Add Client"  # Set the section to Add Client directly

    # Conditionally render the Add Client section based on session state
    if st.session_state["selected_section"] == "Add Client":
        # Add Client Section
        # You can move your "Add Client" logic here or import it from another script
        st.subheader("Add Client")
        name = st.text_input("Client Name")
        age = st.number_input("Age", min_value=0)
        contact = st.text_input("Contact")
        medical_history = st.text_area("Medical History")

        if st.button("Add Client", key="add_client_button"):  # Unique key for the button
            new_entry = {"Name": name, "Age": age, "Contact": contact, "Medical History": medical_history}
            # add_client(new_entry)  # Add the client logic
            st.success("Client Added Successfully!")
            st.balloons()  # Celebrate with balloons!
