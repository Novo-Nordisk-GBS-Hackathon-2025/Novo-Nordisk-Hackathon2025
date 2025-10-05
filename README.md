🧠 Novo-Nordisk-Hackathon2025: 
"A comprehensive market analysis to quantify obesity prevalence, patient profiles, and treatment patterns in India, providing data-driven insights to inform the commercial strategy for Wegovy"

# 👥 Team Members

1. Manish M Kumar (Team Lead)
2. Abhishek Ramesh Shettigar
3. Beven Nelson
4. Elna Sara Sanu
5. Neela KS

# 📘 Project Overview

This Streamlit-based Market Intelligence Dashboard acts as a decision-support engine for Wegovy in India.

It combines NFHS-5 national health survey data, peer-reviewed journals, and industry market reports to identify geographic, demographic, and therapeutic opportunities for obesity management.

🔗 Live Demo:-https://novo-nordisk-hackathon2025-8adxnittedsk6gbmrfbgy3.streamlit.app/

NOTE:🧾 Some datasets are partially hardcoded to preserve reproducibility and accuracy.
All such data points are verified against published research and cited in this README.

🗂️ Core Data Sources (Verified)links are in streamlit app itself
Data Point	Source Type	Reference Link
NFHS-5 Headcount & Prevalence	Peer-reviewed Research	BMC Public Health (2024)

NFHS-5 Spatial Clustering / Hotspots	Peer-reviewed Research	PLOS ONE (2024)

GLP-1 Market Growth (CAGR 2025–2030)	Industry Report	Grand View Research

Anti-Obesity Drug Market Value (Mar 2025)	Economic News	The Economic Times

GLP-1 Patient Openness / Barriers (77.3%)	Academic Journal	IOSR Journal of Pharmacy & Biological Sciences

Bariatric Surgery Cost Range	Market Aggregator	Nobesity India

Lifestyle Intervention Context	Clinical Literature	Frontiers in Endocrinology (2024)
🧩 Dashboard Architecture & Key Analytical Tabs

# Dashboard
The dashboard is divided into three analytical tabs, each focused on strategic decision areas.

🗺️ Tab 1: Geographic & State Rankings
Metric	Source / Derivation	Key Insight
State Rankings	NFHS-5 obesity headcounts (BMC Public Health, 2024)	Top states: Maharashtra, Tamil Nadu, Uttar Pradesh
Comorbidities	are diabetis and hypertension.
Urban vs. Rural	NFHS-5 (Urban Male: 6.6%, Rural Male: 3.3%)	
City Tier Analysis	Derived from NFHS-5 & population clusters	Tier 1 market potential ≈ 85%, Tier 3 ≈ 28%

👥 Tab 2: Gender & Age Segmentation
Metric	Source / Derivation	Key Insight
Gender Prevalence	NFHS-5 (Female: 6.3%, Male: 4.2%)	Female obesity market ≈ 1.5× male
Age Distribution	NFHS-5 + epidemiological estimates	Primary target: 46–60 years

💊 Tab 3: Treatment Options & Market Dynamics
Metric	Source / Derivation	Key Insight
GLP-1 Market Growth	34.3% CAGR (Grand View Research)	Fastest-growing obesity drug segment
Anti-Obesity Drug Market Value	₹576 Crore (Economic Times, 2025)	Large but underpenetrated market
Patient Acceptance	77.3% (IOSR Journal)	High openness to GLP-1-based therapy
Bariatric Cost Barrier	₹2.25–8.0 Lakhs	Wegovy offers affordable non-surgical option
Pharmacological Penetration	Urban 8.5%, Rural 0.8%	Highlights deep urban–rural access gap

⚙️ Tech Stack & Installation
Framework	Streamlit
Data Processing	pandas, Python
Visualization	plotly.express
Language	Python 3.9+

🧭 Setup Instructions
# Install dependencies
pip install streamlit pandas plotly

# Run the dashboard
streamlit run analyis.py

🧮 Backend Architecture

The analytical engine is powered by the StructuredMarketIntelligenceEngine class, which performs:

✅ NFHS-5 Data Parsing (state-level obesity and comorbidity estimation)

✅ Tier-based Market Penetration Scoring

✅ Gender & Age Distribution Modeling

✅ Treatment Landscape Mapping (Lifestyle → GLP-1 → Surgery)

The design emphasizes reproducibility, transparency, and validated reference links within the Streamlit interface.


📊 Strategic Outcomes

>Identifies top 10 high-potential states (Maharashtra, Tamil Nadu, UP, Karnataka, AP, Gujarat, WB, Bihar, Telangana, Kerala).

>Reveals Tier-1 cities hold ~85% of immediate market viability.

>Confirms female-centric and 46–60 years as prime target demographics.

>Demonstrates GLP-1 receptor agonists (like Wegovy) are poised for exponential growth in India’s evolving obesity treatment market.
