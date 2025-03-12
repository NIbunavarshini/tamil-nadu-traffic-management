#!/bin/bash

# Install Python packages using UV
python -m pip install uv
uv pip install streamlit==1.22.0 streamlit-folium==0.11.0 folium==0.14.0 pandas numpy twilio

# Create Streamlit config directory and file
mkdir -p .streamlit
echo '[server]
headless = true
port = 5000
address = "0.0.0.0"' > .streamlit/config.toml

# Run the Streamlit application
streamlit run main.py