import streamlit as st
from utils.map_utils import create_base_map, display_map, add_marker
from data.mock_data import MOCK_EV_STATIONS

def main():
    st.title("EV Charging Stations")

    # Filter section
    col1, col2 = st.columns(2)
    
    with col1:
        search_area = st.text_input("Search Area", "Chennai")
        
    with col2:
        show_available = st.checkbox("Show Only Available Stations", True)

    # Create map
    m = create_base_map()

    # Add EV stations to map
    for station in MOCK_EV_STATIONS:
        if not show_available or station['available']:
            popup_text = f"""
            <b>{station['name']}</b><br>
            Charging Points: {station['charging_points']}<br>
            Status: {'Available' if station['available'] else 'Occupied'}
            """
            add_marker(m, station['location'], popup_text, "plug")

    # Display map
    display_map(m)

    # Station list
    st.subheader("Charging Stations")
    
    cols = st.columns(2)
    for idx, station in enumerate(MOCK_EV_STATIONS):
        with cols[idx % 2]:
            with st.expander(station['name']):
                st.metric("Charging Points", 
                         station['charging_points'])
                
                status = "Available" if station['available'] else "Occupied"
                st.write(f"Status: {status}")
                
                if station['available']:
                    if st.button(f"Book slot at {station['name']}"):
                        st.success("Charging slot booked!")

    # Information section
    st.header("Charging Information")
    
    info_tabs = st.tabs(["Types of Chargers", "Pricing", "Best Practices"])
    
    with info_tabs[0]:
        st.write("""
        - Type 2 AC Charging
        - CCS DC Fast Charging
        - CHAdeMO DC Charging
        """)
        
    with info_tabs[1]:
        st.write("""
        - AC Charging: ₹10-15 per unit
        - DC Fast Charging: ₹20-25 per unit
        - Minimum charge: ₹50
        """)
        
    with info_tabs[2]:
        st.write("""
        - Book in advance during peak hours
        - Check compatibility before charging
        - Follow safety guidelines
        - Monitor charging progress
        """)

    # Sidebar with additional information
    with st.sidebar:
        st.header("Quick Tips")
        st.info("""
        • Check your vehicle's charging compatibility
        • Book slots in advance during peak hours
        • Keep emergency contacts handy
        • Download station-specific apps
        """)

if __name__ == "__main__":
    main()
