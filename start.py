import streamlit as st
import time

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

    # Ensure the session state is initialized
    if "selected_section" not in st.session_state:
        st.session_state["selected_section"] = None

    # Add a single click button for entering the clinic app
    if st.button("کرتە لێرە بکە", key="enter_button"):
        st.session_state["selected_section"] = "Add Client"  # Transition to Add Client section
        time.sleep(1)  # Ensure button press is processed before transitioning
        st.experimental_rerun()  # Re-run the app immediately after button click

    # If the section has been selected, automatically show the add client form (or any next screen)
    if st.session_state.get("selected_section") == "Add Client":
        st.experimental_rerun()  # Force app to show Add Client section after button click
