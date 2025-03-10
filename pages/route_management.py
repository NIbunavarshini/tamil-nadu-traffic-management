import streamlit as st
import folium
from utils.map_utils import create_base_map, display_map, add_marker
from utils.translations import get_text

def main():
    st.title(get_text("route_management_title", "English"))
    
    # Create two columns for origin and destination
    col1, col2 = st.columns(2)
    
    with col1:
        origin = st.text_input(get_text("origin_label", "English"), 
                             "Chennai")
        
    with col2:
        destination = st.text_input(get_text("destination_label", "English"), 
                                  "Coimbatore")

    # Route options
    route_type = st.radio(
        get_text("route_type_label", "English"),
        ["Fastest", "Shortest", "Avoid Tolls"]
    )

    # Create map
    m = create_base_map()
    
    # Example coordinates (Chennai to Coimbatore)
    route_coordinates = [
        [13.0827, 80.2707],  # Chennai
        [11.0168, 76.9558]   # Coimbatore
    ]

    # Draw route line
    folium.PolyLine(
        route_coordinates,
        weight=3,
        color='blue',
        opacity=0.8
    ).add_to(m)

    # Add markers for origin and destination
    add_marker(m, route_coordinates[0], "Chennai", "info-sign")
    add_marker(m, route_coordinates[1], "Coimbatore", "info-sign")

    # Display map
    display_map(m)

    # Traffic alerts section
    st.subheader(get_text("traffic_alerts_title", "English"))
    
    # Mock traffic alerts
    alerts = [
        {"location": "Guindy", "type": "Construction", "delay": "20 mins"},
        {"location": "Salem", "type": "Accident", "delay": "15 mins"}
    ]

    for alert in alerts:
        st.warning(
            f"{alert['location']}: {alert['type']} - Expected delay: {alert['delay']}"
        )

    # Alternative routes
    st.subheader(get_text("alternative_routes_title", "English"))
    
    alt_routes = st.expander("Show Alternative Routes")
    with alt_routes:
        st.write("Route 1: Via Salem - 6 hours")
        st.write("Route 2: Via Trichy - 7 hours")
        st.write("Route 3: Via Madurai - 8 hours")

if __name__ == "__main__":
    main()
