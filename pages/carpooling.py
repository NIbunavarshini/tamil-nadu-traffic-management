import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def main():
    st.title("Carpooling Community")

    # Create/Join Carpool section
    st.header("Create or Join Carpool")
    
    tab1, tab2 = st.tabs(["Create Carpool", "Find Carpool"])

    with tab1:
        with st.form("create_carpool"):
            origin = st.text_input("Starting Point")
            destination = st.text_input("Destination")
            date = st.date_input("Date")
            time = st.time_input("Time")
            seats = st.number_input("Available Seats", 1, 4, 2)
            vehicle = st.text_input("Vehicle Details")
            price = st.number_input("Price per Person (₹)", 0, 1000, 100)
            
            if st.form_submit_button("Create Carpool"):
                st.success("Carpool created successfully!")

    with tab2:
        st.text_input("Search Route", "Chennai to Coimbatore")
        st.date_input("Travel Date")
        
        # Mock available carpools
        mock_carpools = [
            {
                "route": "Chennai to Coimbatore",
                "date": "2024-01-20",
                "time": "07:00",
                "seats": 3,
                "price": "₹500",
                "rating": 4.5
            },
            {
                "route": "Chennai to Coimbatore",
                "date": "2024-01-20",
                "time": "09:00",
                "seats": 2,
                "price": "₹450",
                "rating": 4.2
            }
        ]

        for carpool in mock_carpools:
            with st.expander(f"{carpool['route']} - {carpool['time']}"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Available Seats", carpool['seats'])
                    
                with col2:
                    st.metric("Price", carpool['price'])
                    
                with col3:
                    st.metric("Rating", carpool['rating'])
                    
                if st.button(f"Join this carpool to {carpool['route']}"):
                    st.success("Request sent to the driver!")

    # Community Guidelines
    st.header("Community Guidelines")
    
    guidelines = st.expander("Read Guidelines")
    with guidelines:
        st.write("""
        1. Verify your profile
        2. Be punctual
        3. Share ride expenses fairly
        4. Keep vehicle clean
        5. Follow safety protocols
        6. Communicate clearly
        7. Respect privacy
        """)

    # Safety Features
    with st.sidebar:
        st.header("Safety Features")
        st.info("""
        • Verified Users
        • Real-time Location Sharing
        • Emergency Contacts
        • User Ratings
        • Report System
        """)
        
        st.header("Stats")
        st.metric("Active Users", "1,200+")
        st.metric("Completed Rides", "5,000+")
        st.metric("Average Rating", "4.6/5")

if __name__ == "__main__":
    main()
