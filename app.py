import streamlit as st
import json
import markdown

# Load data from files
def load_gemini_output():
    try:
        with open("gemini_output.md", "r") as f:
            return markdown.markdown(f.read())
    except:
        return None

def load_geojson():
    try:
        with open("west_coast_heat_zones.json", "r") as f:
            return json.load(f)
    except:
        return None

# Streamlit UI
st.title("🌡️ TempTamer: AI-Driven Urban Heat Island Tracker")
st.write(
    "Urban Heat Islands (UHIs) are areas within cities that experience significantly higher "
    "temperatures due to dense infrastructure and low vegetation. TempTamer uses satellite data "
    "and generative AI to detect heat-prone zones and provide data-driven mitigation strategies."
)

st.header("🗺️ Urban Heat Zones on the West Coast")
st.image("static/map_thumbnail.png", use_container_width=True)

gemini_output = load_gemini_output()

st.header("🧠 Gemini-Generated Sustainability Recommendations")
if gemini_output:
    st.subheader("Region-Specific Recommendations (with assumptions):")
    st.table([
        ["Region 1", "Increase tree cover by 20%", "Assumes available land for afforestation"],
        ["Region 2", "Implement reflective roofing", "Assumes buildings have flat roofs"],
        ["Region 3", "Introduce urban water bodies", "Assumes sufficient funding and space"],
    ])
    st.subheader("Other Recommendations:")
    st.markdown(gemini_output, unsafe_allow_html=True)
else:
    st.warning("Gemini recommendations not found. Please run Gemini in Colab and save 'gemini_output.md'.")

st.markdown("---")
st.caption("🔗 Built with Google Earth Engine, Gemini AI, and Streamlit")