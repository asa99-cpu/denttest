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
        st.session_state["selected_section"] = "Welcome"  # Start with the Welcome page

    # Display "Enter Clinic" button
    if st.button("کرتە لێرە بکە", key="enter_button"):
        st.session_state["selected_section"] = "MainApp"  # Set to main app after button click

    # Conditionally render based on selected section
    if st.session_state["selected_section"] == "MainApp":
        show_main_app()

def show_main_app():
    """Main app page containing all sections like Add Client, Client Overview, etc."""
    st.title("Dental Clinic - Main App")

    # Add other sections (Add Client, Client Overview, etc.)
    menu = ["Add Client", "Client Overview", "Appointments", "Medical History"]
    choice = st.sidebar.selectbox("Select a Section", menu)

    if choice == "Add Client":
        add_client_section()
    elif choice == "Client Overview":
        client_overview_section()
    elif choice == "Appointments":
        appointment_section()
    elif choice == "Medical History":
        medical_history_section()

def add_client_section():
    """Section for adding a new client."""
    st.subheader("Add Client")
    name = st.text_input("Client Name")
    age = st.number_input("Age", min_value=0)
    contact = st.text_input("Contact")
    medical_history = st.text_area("Medical History")

    if st.button("Add Client"):
        # Add client logic here
        st.success("Client Added Successfully!")
        st.balloons()  # Celebrate with balloons!

def client_overview_section():
    """Section for viewing all clients."""
    st.subheader("Client Overview")
    # Logic to load and display clients goes here
    st.write("Displaying all clients...")

def appointment_section():
    """Section for viewing appointments."""
    st.subheader("Appointments")
    # Logic for appointments goes here
    st.write("Displaying all appointments...")

def medical_history_section():
    """Section for viewing medical history."""
    st.subheader("Medical History")
    # Logic for medical history goes here
    st.write("Displaying medical history...")

