# Novo-Nordisk-Hackathon2025: Wegovy Market Intelligence Dashboard

## 💊 Wegovy Comprehensive Market Analysis for Strategies
A comprehensive market analysis to quantify obesity prevalence, patient profiles, and treatment patterns in India, providing data-driven insights to inform the commercial strategy for Wegovy.

---

### 👥 Team Members
Manish M Kumar(Team Lead, 
Abhishek Ramesh Shettigar,
Beven Nelson,
Elna Sara Sanu,
Neela KS

---

## 📘 Project Overview
This Streamlit-based dashboard serves as a structured, data-backed **Market Intelligence Engine** for **Wegovy (semaglutide)** in India.

It leverages **NFHS-5 survey data**, **peer-reviewed studies**, and **industry intelligence** to map the commercial landscape, focusing on high-potential geographic targets and patient segments.
**Note:** Some data and analysis points are hardcoded to ensure reproducibility and stability, as detailed below hardcoded data is verified against the real, listed and are  from actual sources that are listed in this readme and clickable links,pdfs and journals on the streamlit app also.
streamlit link-https://novo-nordisk-hackathon2025-8adxnittedsk6gbmrfbgy3.streamlit.app/



## 🗂️ Core Data Sources (Verified)
| Data Point | Source Type | Reference Link |
| :--- | :--- | :--- |
| **NFHS-5 Headcount & Prevalence** | Peer-reviewed Research | [https://doi.org/10.1186/s12889-024-18784-4](https://doi.org/10.1186/s12889-024-18784-4) |
| **NFHS-5 Spatial Clustering/Hotspots** | Peer-reviewed Research | [https://doi.org/10.1371/journal.pone.0305205](https://doi.org/10.1371/journal.pone.0305205) |
| **GLP-1 Market Growth Rate (CAGR 2025-2030)** | Industry Report | [https://www.grandviewresearch.com/industry-analysis/india-glp-1-receptor-agonist-market-report](https://www.grandviewresearch.com/industry-analysis/india-glp-1-receptor-agonist-market-report) |
| **Anti-Obesity Drug Market Value (Mar 2025)** | Economic News | [https://m.economictimes.com/industry/healthcare/biotech/pharmaceuticals/a-big-fat-fight-has-just-broken-out-in-india/articleshow/122049705.cms](https://m.economictimes.com/industry/healthcare/biotech/pharmaceuticals/a-big-fat-fight-has-just-broken-out-in-india/articleshow/122049705.cms) |
| **GLP-1 Patient Openness/Barriers (77.3%)** | Academic Journal | [https://www.iosrjournals.org/iosr-jpbs/papers/Vol19-issue6/Ser-2/L1906027179.pdf](https://www.iosrjournals.org/iosr-jpbs/papers/Vol19-issue6/Ser-2/L1906027179.pdf) |
| **Bariatric Surgery Cost Range** | Market Aggregator/Clinic | [https://nobesity.in/weight-loss-surgery-cost-in-india/](https://nobesity.in/weight-loss-surgery-cost-in-india/) |
| **Lifestyle Intervention Context** | Clinical Literature | [https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1382814/full](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1382814/full) |

---

## 🧩 Detailed Dashboard Features and Methodology

The dashboard is organized into three primary Streamlit tabs for clarity, representing the core analytical areas for commercial strategy.

### **🗺️ Tab 1: Geographic & Rankings**

| Metric | Source / Derivation | Key Insight |
| :--- | :--- | :--- |
| **State Rankings** | NFHS-5 raw patient headcounts (BMI> 30.0) from BMC Public Health article. | Ranks states by absolute volume of obese patients (e.g., Maharashtra, Tamil Nadu). |
| **Comorbidities** | Calculated via epidemiological multipliers (e.g., Diabetes $\approx 2.1\times$ Obesity rate). | Identifies regions with high potential for medically indicated use cases (BMI $\ge 27$ with comorbidity). |
| **Urban vs. Rural Prevalence** | NFHS-5 data (Urban Male: 6.6%, Rural Male: 3.3%). | Highlights the **2x higher** prevalence in urban areas, confirming initial market focus. |
| **City Tier Analysis** | Hardcoded logic based on state groupings (Tier 1 includes Maharashtra, TN, Karnataka, etc.). | Maps **Market Penetration Potential** (T1: 85%, T3: 28%) to guide city selection. |

### **👥 Tab 2: Gender & Age Segmentation**

| Metric | Source / Derivation | Key Insight |
| :--- | :--- | :--- |
| **Gender Prevalence** | NFHS-5 validated data (Female: 6.3%, Male: 4.2%). | **Female patients present a 50% larger potential market** by overall prevalence. |
| **Age Distribution** | Estimated distribution based on NFHS-5 trends and general epidemiology. | Pinpoints the prime target cohort for intervention (estimated to be **46-60** years). |

### **💊 Tab 3: Treatment Options: Market Dynamics**

| Metric | Source / Derivation | Key Insight |
| :--- | :--- | :--- |
| **GLP-1 Market Growth** | Verified: **34.3% CAGR** (Grand View Research). | Confirms the rapid expansion and commercial viability of the segment. |
| **AOD Market Value** | Verified: **₹576.0 Crore** (Economic Times). | Benchmarks the current size of the overall Anti-Obesity Drug market. |
| **Patient Acceptance** | Verified: **77.3% Openness** (IOSR Journal). | High acceptance validates a shift away from traditional, less effective interventions. |
| **Bariatric Cost Barrier** | Verified: **₹2.25-8.0 Lakhs** cost range. | Positions Wegovy as a significantly more affordable, non-surgical alternative for millions. |
| **Pharmacological Penetration** | Estimated (Urban: 8.5%, Rural: 0.8%). | Quantifies the massive **penetration gap** between high-affluence urban centers and the rest of India. |

---

## ⚙️ Tech Stack & Installation

| Layer | Technology |
| :--- | :--- |
| **Framework** | **Streamlit** |
| **Data Processing** | `pandas`, Python  |
| **Visualization** | `plotly.express` |
| **Language** | Python 3.9+ |


#  Install core dependencies (based on code usage)
pip install streamlit pandas plotly

#  Run Streamlit app
streamlit run app.py
