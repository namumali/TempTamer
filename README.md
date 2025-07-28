*** TempTamer: Urban Heat Zone Analysis and Cooling Strategy Recommendations ***

# Overview

   TempTamer is an AI-driven project designed to identify urban heat zones using satellite data and provide actionable cooling strategy recommendations. Leveraging Google Earth Engine (GEE) for land surface temperature (LST) extraction and Google Gemini for AI-generated advisory, TempTamer helps urban planners and environmental scientists mitigate heat island effects.

# Features

   LST Extraction: Calculates land surface temperature over user-defined regions.

   Urban Heat Zone Mapping: Visualizes high-heat areas with interactive maps.

   AI-Driven Recommendations: Uses Gemini to generate tailored cooling strategies (e.g., vegetation planting, reflective materials).

   Notebook Workflow: Fully documented Jupyter notebook to reproduce analysis in Google Colab or local environment.

# Getting Started

Prerequisites

   Python 3.8+

   Google Earth Engine account (sign up at https://earthengine.google.com)

   Google Cloud SDK (for GEE authentication) or Colab environment

   Gemini API access (provide GEMINI_API_KEY)

# Installation

Clone this repository:

   git clone https://github.com/your-username/TempTamer.git
   cd TempTamer

# Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate      # Windows

# Install dependencies:

   pip install -r requirements.txt

   Authenticate with Google Earth Engine:

   earthengine authenticate

# Usage

Google Colab

Open TempTamer.ipynb in Google Colab.

Set environment variables in the first cell:

   import os
   os.environ['GEMINI_API_KEY'] = 'your_gemini_api_key'

Run all cells sequentially to reproduce the analysis and generate maps.

Local Jupyter Notebook

Start Jupyter:

   jupyter notebook

Open TempTamer.ipynb.

Ensure GEE credentials and GEMINI_API_KEY are set in your shell or notebook.

# File Structure
   TempTamer/
   ├── TempTamer.ipynb       # Main analysis notebook
   ├── requirements.txt      # Python dependencies
   ├── data/                 # (Optional) sample data or region definitions
   ├── maps/                 # Generated heat zone maps
   └── README.md             # Project documentation
