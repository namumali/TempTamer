# TempTamer 🌡️

TempTamer is an AI-powered platform designed to analyze urban heat zones using satellite data and provide actionable, data-driven strategies to mitigate Urban Heat Island (UHI) effects through sustainable urban planning.

## Features 🚀

- **Urban Heat Zone Mapping**: Visualize heat-prone areas on an interactive map.
- **AI-Generated Recommendations**: Leverage AI to generate sustainability strategies tailored to specific regions.
- **Region-Specific Insights**: Detailed recommendations for mitigating UHI effects, including assumptions and estimated impacts.
- **Customizable Data Inputs**: Supports GeoJSON data for heat zones and Markdown-based AI outputs for recommendations.
- **Sustainability Planning**: Provides strategies such as afforestation, cool pavements, green roofs, and urban design improvements.

## How It Works 🛠️

1. **Data Input**:
   - Heat zone data is loaded from a GeoJSON file (`west_coast_heat_zones.json`).
   - AI-generated recommendations are read from a Markdown file (`gemini_output.md`).

2. **Processing**:
   - The platform uses Flask to render a web-based UI.
   - AI recommendations are parsed and displayed in a structured format, including tables for region-specific insights.

3. **Visualization**:
   - A map thumbnail (`map_thumbnail.png`) is displayed to provide a visual overview of urban heat zones.
   - Recommendations are categorized into region-specific and strategic insights.

## Installation 🖥️

Follow these steps to set up and run TempTamer locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/TempTamer.git
   cd TempTamer
