# 🧠 Novo Nordisk GBS Hackathon 2025
A comprehensive market analysis to quantify obesity prevalence, patient profiles, and treatment patterns in India, providing data-driven insights to inform the commercial strategy for Wegovy

👥 Team Members
1. Manish M Kumar (Team Lead)
2. Abhishek Ramesh Shettigar
3. Beven Nelson
4. Elna Sara Sanu
5. Neela KS

# 📘 Project Overview

This Streamlit-based Market Intelligence Dashboard acts as a decision-support engine for Wegovy in India.

It combines NFHS-5 national health survey data, peer-reviewed journals, and industry market reports to identify geographic, demographic, and therapeutic opportunities for obesity management.

🔗 Live Demo: https://novo-nordisk-hackathon2025-8adxnittedsk6gbmrfbgy3.streamlit.app/

🧾 NOTE: analysis.py consists of streamlit code
backend_process is the process of extraction for the streamlit values that are coded 
for more analysis, and strategies framed are in the PPT
Some data are  hardcoded to preserve reproducibility and accuracy. All such data points are verified against published research and cited in this README.

🗂️ Core Data Sources (Verified)
1. Data Point	Source Type	Reference Link
2. NFHS-5 Headcount & Prevalence	Peer-reviewed Research	BMC Public Health (2024)
3. NFHS-5 Spatial Clustering / Hotspots	Peer-reviewed Research	PLOS ONE (2024)
4. GLP-1 Market Growth (CAGR 2025–2030)	Industry Report	Grand View Research
5. Anti-Obesity Drug Market Value (Mar 2025)	Economic News	The Economic Times
6. GLP-1 Patient Openness / Barriers (77.3%)	Academic Journal	IOSR Journal of Pharmacy & Biological Sciences
7. Bariatric Surgery Cost Range	Market Aggregator	Nobesity India
8. Lifestyle Intervention Context	Clinical Literature	Frontiers in Endocrinology (2024)

# 🧩 Dashboard Architecture & Key Analytical Tabs

The dashboard is divided into three analytical tabs, each focused on strategic decision areas.

## 🗺️ Tab 1: Geographic & State Rankings
- Metric	Source / Derivation	Key Insight
- State Rankings	NFHS-5 obesity headcounts (BMC Public Health, 2024). Top states: Maharashtra, Tamil Nadu, Uttar Pradesh. Comorbidities: diabetes, hypertension.
- Urban vs. Rural	NFHS-5 (Urban Male: 6.6%, Rural Male: 3.3%)	Significant urban–rural gap.
- City Tier Analysis	Derived from NFHS-5 & population clusters	Tier 1 market potential ≈ 85%, Tier 3 ≈ 28%.

## 👥 Tab 2: Gender & Age Segmentation
- Metric	Source / Derivation	Key Insight
- Gender Prevalence	NFHS-5 (Female: 6.3%, Male: 4.2%)	Female obesity market ≈ 1.5× male.
- Age Distribution	NFHS-5 + epidemiological estimates	Primary target: 46–60 years.

## 💊 Tab 3: Treatment Options & Market Dynamics
- Metric	Source / Derivation	Key Insight
- GLP-1 Market Growth	34.3% CAGR (Grand View Research)	Fastest-growing obesity drug segment.
- Anti-Obesity Drug Market Value	₹576 Crore (Economic Times, 2025)	Large but underpenetrated market.
- Patient Acceptance	77.3% (IOSR Journal)	High openness to GLP-1-based therapy.
- Bariatric Cost Barrier	₹2.25–8.0 Lakhs	Wegovy offers an affordable non-surgical option.
- Pharmacological Penetration	Urban 8.5%, Rural 0.8%	Highlights deep urban–rural access gap.
 
## ⚙️ Tech Stack & Installation
- Framework: Streamlit
- Data Processing: pandas, Python
- Visualization: plotly.express
- Language: Python 3.9+

# 🧭 Setup Instructions

## Install dependencies
pip install streamlit pandas plotly

## Run the dashboard
streamlit run analyis.py

## 🧮 Backend Architecture

The analytical engine is powered by the StructuredMarketIntelligenceEngine class, which performs:

- ✅ NFHS-5 Data Parsing (state-level obesity and comorbidity estimation)
- ✅ Tier-based Market Penetration Scoring
- ✅ Gender & Age Distribution Modelling
- ✅ Treatment Landscape Mapping (Lifestyle → GLP-1 → Surgery)

The design emphasises reproducibility, transparency, and validated reference links within the Streamlit interface.

## 📊 Strategic Outcomes
- Identifies top 10 high-potential states (Maharashtra, Tamil Nadu, UP, Karnataka, AP, Gujarat, WB, Bihar, Telangana, Kerala).
- Reveals Tier-1 cities hold ~85% of immediate market viability.
- Confirms female-centric and 46–60 years as the prime target demographics.
- Demonstrates GLP-1 receptor agonists (like Wegovy) are poised for exponential growth in India’s evolving obesity treatment market.

# 💼 Commercial Strategy for Wegovy (Semaglutide) in India

This market analysis outlines a commercial strategy for introducing Wegovy (semaglutide) in India, addressing the nation's rising obesity crisis.

🇮🇳 The Indian Obesity Crisis and Market Gap

India is facing an obesity epidemic with low structured treatment adoption and limited awareness among patients and healthcare providers. Traditional approaches are insufficient for managing the scale and complexity of obesity in the country’s diverse healthcare landscape.

## 💉 Wegovy: Efficacy and Target Population
Wegovy is a once-weekly injectable medication that has been clinically proven to deliver significant weight loss (~15%) in adults, while also improving metabolic outcomes.

Eligibility and Indication:
- Individuals aged 12 years and older with obesity, or overweight with comorbidities.
- Adults with BMI ≥30, or BMI ≥27 with diabetes, hypertension, or cardiovascular risk factors.

## ⚖️ Competitive Landscape
Wegovy competes with:
- Mounjaro (Tirzepatide)
- Lifestyle interventions
- Bariatric surgery
- Nutraceuticals / OTC weight-loss products

## 📈 Market Sizing and Prevalence
Metric	Estimate
- Potential Patients	~85 million adults eligible for Wegovy
- Obesity Prevalence (2021)	5.8% overall (Women: 6.3%, Men: 4.2%)
- Rising Trend	2–3× increase since 2000
- urban–Rural gap	Urban ≈ 2× rural prevalence

## 🗺️ Geographic Focus
Focus on Tier 1 & Tier 2 cities, with high opportunity in these top states:
- Maharashtra (4.7M)
- Tamil Nadu (3.8M)
- Uttar Pradesh (3.7M)
- Karnataka (3.5M)
- Andhra Pradesh (3.2M)

## 🎯 Target Channels
- Healthcare Facilities: Hospitals, obesity clinics, and wellness centres offering structured weight programs.
- Healthcare Providers: Endocrinologists, obesity specialists, and primary care physicians.
- Patients: Individuals seeking medically supervised, long-term weight management solutions.

# 🧩 Strategic Recommendations
1. 🩺 Obesity Awareness Initiatives
- Free Health Camps: BMI checks, basic tests, brochures, and family history screening.
- VR Awareness Campaign: Immersive “life with poor health choices” experience.
- Social Media Posters: Shareable visuals promoting healthy lifestyles.

2. 🎓 Conferences & Workshops
- Obesity Summits: Partner with IMA, RSSDI, and Endocrine Society of India.
- Clinical Workshops: Train HCPs on eligibility, dosage, adherence, and side-effect management with visual transformation demos.

3. 📱 Smart Wellness App & AI Chatbot
- Features: Track weight, provide AI guidance, connect to doctors, send reminders, and log lifestyle feedback.
- Retention: Launch “Wegovy Care” — weekly consultations, dietitian calls, dose reminders, and reward points.

4. 💡 Other Strategies & Incentives
- Influencer Collaborations: Promote obesity awareness and modern solutions.
- HCP Recognition: Awards and speaking opportunities at Novo Nordisk forums.
- Patient Adherence Rewards: Points for milestones (3M, 6M, 1Y).
- Pharmacy Incentives: Tiered programs (Silver/Gold/Platinum) based on refill and sales milestones.
