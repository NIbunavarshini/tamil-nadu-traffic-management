
#!/bin/bash

# Install Python packages
pip install streamlit==1.22.0 streamlit-folium==0.11.0 folium==0.14.0 pandas numpy twilio

# Create Streamlit config directory and file
mkdir -p .streamlit
echo '[server]
headless = true
port = 5000
address = "0.0.0.0"' > .streamlit/config.toml

# Create a simple start script that Vercel will run
echo '#!/bin/bash
streamlit run main.py --server.headless=true --server.port=5000 --server.address=0.0.0.0' > start.sh
chmod +x start.sh
