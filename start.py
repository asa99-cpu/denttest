import streamlit as st
import time

def display_welcome_animation():
    """Display animation or attractive page."""
    st.title("Welcome to the Dental Clinic App")

    # Display some fancy animation or text effect
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
    </style>
    <div class="welcome-text">
        <h1>Welcome to Our Clinic!</h1>
        <p>We're glad to have you here. Click below to get started!</p>
    </div>
    """, unsafe_allow_html=True)

    # Add some delay to let the animation load
    time.sleep(2)

    # Add buttons to navigate after animation
    if st.button("Enter Clinic App"):
        st.session_state["selected_section"] = "Add Client"  # Update session state to move to the app
        # No rerun here, just let the flow continue naturally

