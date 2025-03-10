import folium
import streamlit as st
from streamlit_folium import folium_static

def create_base_map():
    """Create a base map centered on Tamil Nadu"""
    return folium.Map(
        location=[11.1271, 78.6569],
        zoom_start=7,
        tiles='OpenStreetMap'
    )

def add_marker(map_obj, location, popup, icon=None):
    """Add a marker to the map"""
    if icon:
        folium.Marker(
            location=location,
            popup=popup,
            icon=folium.Icon(icon=icon)
        ).add_to(map_obj)
    else:
        folium.Marker(
            location=location,
            popup=popup
        ).add_to(map_obj)

def display_map(map_obj):
    """Display a folium map in Streamlit"""
    folium_static(map_obj)
