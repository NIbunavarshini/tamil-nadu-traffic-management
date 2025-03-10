import streamlit as st
import pandas as pd
from utils.map_utils import create_base_map, display_map, add_marker
from data.mock_data import MOCK_PARKING_SPOTS

def main():
    st.title("Parking Space Finder")

    # Search and filter section
    col1, col2 = st.columns(2)
    
    with col1:
        search_area = st.text_input("Search Area", "Chennai")
        
    with col2:
        filter_available = st.checkbox("Show Only Available Spots", True)

    # Create map
    m = create_base_map()

    # Add parking spots to map
    for spot in MOCK_PARKING_SPOTS:
        if not filter_available or spot['available_spots'] > 0:
            popup_text = f"""
            <b>{spot['name']}</b><br>
            Available: {spot['available_spots']}/{spot['total_spots']}
            """
            add_marker(m, spot['location'], popup_text, "parking")

    # Display map
    display_map(m)

    # Parking spot list
    st.subheader("Available Parking Spots")
    
    for spot in MOCK_PARKING_SPOTS:
        if not filter_available or spot['available_spots'] > 0:
            with st.expander(spot['name']):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Available Spots", 
                             spot['available_spots'])
                    
                with col2:
                    st.metric("Total Capacity", 
                             spot['total_spots'])
                    
                if st.button(f"Reserve at {spot['name']}"):
                    st.success("Booking request sent! Please arrive within 30 minutes.")

    # Parking tips
    with st.sidebar:
        st.subheader("Smart Parking Tips")
        st.info("""
        • Book in advance during peak hours
        • Check for special event parking
        • Consider park-and-ride options
        • Look for early bird specials
        """)

if __name__ == "__main__":
    main()
