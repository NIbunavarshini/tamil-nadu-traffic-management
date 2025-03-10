import streamlit as st
import folium
from utils.map_utils import create_base_map, display_map, add_marker
from utils.translations import get_text
from data.mock_data import MAJOR_CITIES

def main():
    st.title(get_text("route_management_title", "English"))

    # Create two columns for origin and destination
    col1, col2 = st.columns(2)

    city_names = [city["name"] for city in MAJOR_CITIES]

    with col1:
        origin = st.selectbox(
            get_text("origin_label", "English"),
            options=city_names,
            index=city_names.index("Chennai") if "Chennai" in city_names else 0
        )

    with col2:
        # Filter out origin city from destination options
        dest_options = [city for city in city_names if city != origin]
        destination = st.selectbox(
            get_text("destination_label", "English"),
            options=dest_options,
            index=dest_options.index("Coimbatore") if "Coimbatore" in dest_options else 0
        )

    # Route options
    route_type = st.radio(
        get_text("route_type_label", "English"),
        ["Fastest", "Shortest", "Avoid Tolls"]
    )

    # Create map
    m = create_base_map()

    # Get coordinates for selected cities
    origin_coords = next(city["location"] for city in MAJOR_CITIES if city["name"] == origin)
    dest_coords = next(city["location"] for city in MAJOR_CITIES if city["name"] == destination)

    # Draw route line
    folium.PolyLine(
        [origin_coords, dest_coords],
        weight=3,
        color='blue',
        opacity=0.8
    ).add_to(m)

    # Add markers for all major cities
    for city in MAJOR_CITIES:
        icon = None
        if city["name"] == origin:
            icon = "play"
        elif city["name"] == destination:
            icon = "stop"

        add_marker(m, city["location"], city["name"], icon)

    # Display map
    display_map(m)

    # Traffic alerts section
    st.subheader(get_text("traffic_alerts_title", "English"))

    # Mock traffic alerts
    alerts = [
        {"location": "Guindy", "type": "Construction", "delay": "20 mins"},
        {"location": "Salem", "type": "Accident", "delay": "15 mins"},
        {"location": "Trichy", "type": "Road Work", "delay": "25 mins"}
    ]

    for alert in alerts:
        st.warning(
            f"{alert['location']}: {alert['type']} - Expected delay: {alert['delay']}"
        )

    # Alternative routes
    st.subheader(get_text("alternative_routes_title", "English"))

    with st.expander("Show Alternative Routes"):
        st.write(f"Route 1: Via Salem - Estimated time: 6 hours")
        st.write(f"Route 2: Via Trichy - Estimated time: 7 hours")
        st.write(f"Route 3: Via Madurai - Estimated time: 8 hours")

if __name__ == "__main__":
    main()