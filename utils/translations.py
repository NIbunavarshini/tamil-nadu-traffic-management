TRANSLATIONS = {
    "main_title": {
        "English": "Tamil Nadu Traffic Management System",
        "தமிழ்": "தமிழ்நாடு போக்குவரத்து மேலாண்மை அமைப்பு"
    },
    "features_header": {
        "English": "Available Features",
        "தமிழ்": "கிடைக்கும் வசதிகள்"
    },
    "features_list": {
        "English": """
        * Route Management
        * Parking Space Finder
        * Emergency Response
        * EV Charging Stations
        * Carpooling Services
        * FASTag Balance
        * Construction Reports
        """,
        "தமிழ்": """
        * பாதை மேலாண்மை
        * வாகன நிறுத்துமிடம் கண்டுபிடிப்பான்
        * அவசர பதில்
        * மின்சார வாகன சார்ஜிங் நிலையங்கள்
        * கார்பூலிங் சேவைகள்
        * FASTag இருப்பு
        * கட்டுமான அறிக்கைகள்
        """
    },
    "route_management_title": {
        "English": "Route Management",
        "தமிழ்": "பாதை மேலாண்மை"
    },
    "origin_label": {
        "English": "Starting Point",
        "தமிழ்": "தொடக்க இடம்"
    },
    "destination_label": {
        "English": "Destination",
        "தமிழ்": "சேரும் இடம்"
    },
    "route_type_label": {
        "English": "Route Type",
        "தமிழ்": "பாதை வகை"
    },
    "traffic_alerts_title": {
        "English": "Traffic Alerts",
        "தமிழ்": "போக்குவரத்து எச்சரிக்கைகள்"
    },
    "alternative_routes_title": {
        "English": "Alternative Routes",
        "தமிழ்": "மாற்று பாதைகள்"
    },
    "report_accident": {
        "English": "Report Accident",
        "தமிழ்": "விபத்து அறிக்கை"
    },
    "find_parking": {
        "English": "Find Parking",
        "தமிழ்": "வாகன நிறுத்துமிடம் தேடல்"
    },
    "ev_charging": {
        "English": "EV Charging Stations",
        "தமிழ்": "மின்சார வாகன நிலையங்கள்"
    },
    "traffic_caption": {
        "English": "Real-time traffic management",
        "தமிழ்": "நேரடி போக்குவரத்து மேலாண்மை"
    },
    "transport_caption": {
        "English": "Smart transportation solutions",
        "தமிழ்": "திறன்மிகு போக்குவரத்து தீர்வுகள்"
    },
    "quick_actions": {
        "English": "Quick Actions",
        "தமிழ்": "விரைவு செயல்கள்"
    },
    "footer_text": {
        "English": "© 2025 Tamil Nadu Traffic Management System",
        "தமிழ்": "© 2025 தமிழ்நாடு போக்குவரத்து மேலாண்மை அமைப்பு"
    }
}

def get_text(key, language):
    """Get translated text for given key and language"""
    return TRANSLATIONS.get(key, {}).get(language, f"Translation missing for: {key}")