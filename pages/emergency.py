import streamlit as st
from data.mock_data import EMERGENCY_CONTACTS, FIRST_AID_STEPS
from utils.map_utils import create_base_map, display_map, add_marker

def main():
    st.title("Emergency Response System")

    # Emergency contact numbers
    st.header("Emergency Contacts")
    
    cols = st.columns(len(EMERGENCY_CONTACTS))
    for col, (service, number) in zip(cols, EMERGENCY_CONTACTS.items()):
        with col:
            st.button(f"{service}: {number}")

    # Accident reporting form
    st.header("Report an Accident")
    
    with st.form("accident_report"):
        location = st.text_input("Location")
        severity = st.select_slider(
            "Incident Severity",
            options=["Minor", "Moderate", "Severe", "Critical"]
        )
        description = st.text_area("Description")
        need_ambulance = st.checkbox("Need Ambulance?")
        
        submitted = st.form_submit_button("Submit Report")
        
        if submitted:
            st.success("Emergency services have been notified!")
            if need_ambulance:
                st.info("Ambulance has been dispatched to your location")

    # First aid instructions
    st.header("First Aid Instructions")
    
    for step in FIRST_AID_STEPS:
        with st.expander(step['title']):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(step['image_url'], 
                        caption=step['title'])
                
            with col2:
                st.write(step['description'])

    # Emergency rerouting
    st.header("Emergency Rerouting")
    
    # Create map for rerouting
    m = create_base_map()
    
    # Example accident location
    accident_location = [13.0827, 80.2707]
    add_marker(m, accident_location, "Accident Location", "warning-sign")

    # Display alternative routes
    folium.PolyLine(
        [[13.0827, 80.2707], [13.0500, 80.2500], [13.0300, 80.2300]],
        color="green",
        weight=3,
        opacity=0.8
    ).add_to(m)

    display_map(m)

    # Safety tips
    with st.sidebar:
        st.header("Safety Tips")
        st.info("""
        • Stay calm and assess the situation
        • Ensure your safety first
        • Call emergency services immediately
        • Use hazard lights to warn other vehicles
        • Keep first aid kit in your vehicle
        """)

if __name__ == "__main__":
    main()
