#!/bin/bash
pip install -r requirements.txt
mkdir -p .streamlit
echo '[server]
headless = true
port = 5000
address = "0.0.0.0"' > .streamlit/config.toml
streamlit run main.py