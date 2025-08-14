# from flask import Flask, render_template_string, jsonify, url_for
# import json
# import os
# import markdown

# app = Flask(__name__)

# # Load data from files
# def load_gemini_output():
#     try:
#         with open("gemini_output.md", "r") as f:
#             return markdown.markdown(f.read())  # Convert Markdown to HTML
#     except:
#         return None

# def load_geojson():
#     try:
#         with open("west_coast_heat_zones.json", "r") as f:
#             return json.load(f)
#     except:
#         return None

# @app.route("/")
# def index():
#     gemini_output = load_gemini_output()
#     geojson_data = load_geojson()
    
#     html = """
#     <html>
#     <head>
#         <title>TempTamer - Urban Heat Island Tracker</title>
#         <style>
#             body { font-family: Arial, sans-serif; margin: 20px; background: #f7f9fa; color: #333; }
#             h1, h2 { color: #00796B; }
#             .map-section, .ai-section { margin-bottom: 40px; }
#             .map-section img { border: 1px solid #ccc; border-radius: 5px; }
#             .footer { margin-top: 40px; font-size: 0.9em; color: #888; text-align: center; }
#             .recommendations { background: #fff; border: 1px solid #ccc; padding: 15px; border-radius: 5px; }
#             .recommendations h3 { color: #00796B; margin-top: 0; }
#             table { width: 100%; border-collapse: collapse; margin-top: 20px; }
#             table, th, td { border: 1px solid #ccc; }
#             th, td { padding: 10px; text-align: left; }
#             th { background-color: #f2f2f2; }
#         </style>
#     </head>
#     <body>
#         <h1>🌡️ TempTamer: AI-Driven Urban Heat Island Tracker</h1>
#         <p>Urban Heat Islands (UHIs) are areas within cities that experience significantly higher temperatures due to dense infrastructure and low vegetation.
#         TempTamer uses satellite data and generative AI to detect heat-prone zones and provide data-driven mitigation strategies.</p>

#         <div class="map-section">
#             <h2>🗺️ Urban Heat Zones on the West Coast</h2>
#             <img src="{{ url_for('static', filename='map_thumbnail.png') }}" width="100%" alt="Heat Zone Map" />
#         </div>

#         <div class="ai-section">
#             <h2>🧠 Gemini-Generated Sustainability Recommendations</h2>
#             {% if gemini_output %}
#                 <div class="recommendations">
#                     <h3>Region-Specific Recommendations (with assumptions):</h3>
#                     <table>
#                         <thead>
#                             <tr>
#                                 <th>Region</th>
#                                 <th>Recommendation</th>
#                                 <th>Assumptions</th>
#                             </tr>
#                         </thead>
#                         <tbody>
#                             <tr>
#                                 <td>Region 1</td>
#                                 <td>Increase tree cover by 20%</td>
#                                 <td>Assumes available land for afforestation</td>
#                             </tr>
#                             <tr>
#                                 <td>Region 2</td>
#                                 <td>Implement reflective roofing</td>
#                                 <td>Assumes buildings have flat roofs</td>
#                             </tr>
#                             <tr>
#                                 <td>Region 3</td>
#                                 <td>Introduce urban water bodies</td>
#                                 <td>Assumes sufficient funding and space</td>
#                             </tr>
#                         </tbody>
#                     </table>
#                     <h3>Other Recommendations:</h3>
#                     {{ gemini_output | safe }}
#                 </div>
#             {% else %}
#                 <div class="recommendations">
#                     <h3>Region-Specific Recommendations (with assumptions):</h3>
#                     <table>
#                         <thead>
#                             <tr>
#                                 <th>Region</th>
#                                 <th>Recommendation</th>
#                                 <th>Assumptions</th>
#                             </tr>
#                         </thead>
#                         <tbody>
#                             <tr>
#                                 <td colspan="3" style="text-align: center;">
#                                     <i>Gemini recommendations not found. Please run Gemini in Colab and save 'gemini_output.md'.</i>
#                                 </td>
#                             </tr>
#                         </tbody>
#                     </table>
#                 </div>
#             {% endif %}
#         </div>

#         <div class="footer">
#             <hr>
#             <p>🔗 Built with Google Earth Engine, Gemini AI, and Flask</p>
#         </div>
#     </body>
#     </html>
#     """

#     return render_template_string(html, gemini_output=gemini_output)

# if __name__ == "__main__":
#     app.run(debug=True)


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