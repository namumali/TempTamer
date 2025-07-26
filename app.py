import streamlit as st
import json
import os

st.set_page_config(layout="wide", page_title="TempTamer", page_icon="🌡️")

# Title
st.title("🌡️ TempTamer: AI-Driven Urban Heat Island Tracker")

# Introduction
st.markdown(
    """
    Urban Heat Islands (UHIs) are areas within cities that experience significantly higher temperatures due to dense infrastructure and low vegetation.
    TempTamer uses satellite data and generative AI to detect heat-prone zones and provide data-driven mitigation strategies.
    """
)

# Section: Heat Zone Map
st.header("🗌️ Urban Heat Zones on the West Coast")

if os.path.exists("map_thumbnail.png"):
    st.image("map_thumbnail.png", caption="Google Earth Engine Heat Zone Map (Surface Temp > 37°C)", use_column_width=True)
else:
    st.info("Map preview not found. Please export 'map_thumbnail.png' from your Colab notebook.")

# Section: AI Recommendations
st.header("🧠 Gemini-Generated Sustainability Recommendations")

if os.path.exists("gemini_output.md"):
    with open("gemini_output.md", "r") as f:
        gemini_markdown = f.read()
    st.markdown(gemini_markdown, unsafe_allow_html=True)
else:
    st.warning("Gemini recommendations not found. Please run Gemini in Colab and save 'gemini_output.md'.")

# Optional: Expandable raw GeoJSON data view
with st.expander("📦 View Raw Heat Zone GeoJSON"):
    if os.path.exists("west_coast_heat_zones.json"):
        with open("west_coast_heat_zones.json", "r") as f:
            geojson_data = json.load(f)
        st.json(geojson_data)
    else:
        st.info("GeoJSON data not found. Please save 'west_coast_heat_zones.json' from Colab.")

# Footer
st.markdown("---")
st.markdown("🔗 Built with Google Earth Engine, Gemini AI, and Streamlit")
