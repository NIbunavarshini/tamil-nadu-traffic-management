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
    # Add more translations as needed
}

def get_text(key, language):
    """Get translated text for given key and language"""
    return TRANSLATIONS.get(key, {}).get(language, "Translation missing")
