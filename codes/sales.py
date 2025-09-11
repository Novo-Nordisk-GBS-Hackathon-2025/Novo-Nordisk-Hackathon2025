# sales_dashboard.py
import streamlit as st
import pandas as pd
import feedparser
import requests
import random
import time
from bs4 import BeautifulSoup
import plotly.express as px
from io import BytesIO

# -------------------------
# 1. Scraper: Multi-Source Pharma Headlines
# -------------------------
def scrape_news_headlines(keywords, pages=2, max_rss=20):
    records = []

    # A) Google News RSS (most reliable)
    for kw in keywords:
        rss_url = f"https://news.google.com/rss/search?q={kw}+pharma+india"
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:max_rss]:
            records.append({
                "source": "Google News",
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", ""),
                "keyword": kw
            })

    # B) MoneyControl + BusinessToday
    sources = [
        {"name": "MoneyControl", "url": "https://www.moneycontrol.com/news/business/pharma/"},
        {"name": "BusinessToday", "url": "https://www.businesstoday.in/latest/economy"}
    ]
    for src in sources:
        for p in range(1, pages + 1):
            try:
                url = src["url"] + (f"page-{p}" if p > 1 else "")
                r = requests.get(url, timeout=10)
                soup = BeautifulSoup(r.text, "html.parser")
                links = soup.find_all("a", href=True)
                for a in links:
                    text = a.get_text(strip=True)
                    href = a["href"]
                    if any(k.lower() in text.lower() for k in keywords):
                        records.append({
                            "source": src["name"],
                            "title": text,
                            "link": href,
                            "published": "",
                            "keyword": ", ".join(keywords)
                        })
                time.sleep(0.5)
            except:
                continue

    return pd.DataFrame(records)

# -------------------------
# 2. Mock State Sales Generator
# -------------------------
INDIA_STATES = [
    "Maharashtra","Karnataka","Tamil Nadu","Uttar Pradesh","Gujarat","Delhi",
    "Rajasthan","West Bengal","Telangana","Andhra Pradesh","Kerala","Bihar",
    "Punjab","Haryana","Chhattisgarh","Odisha","Jharkhand","Assam","Goa","Manipur"
]

def generate_mock_state_sales(drug_names, from_date, to_date, seed=42):
    random.seed(seed)
    rows = []
    base_totals = {
        "Rybelsus": 412_000_000,
        "Mounjaro": 98_000_000,
        "Wegovy": 7_000_000
    }
    for drug in drug_names:
        total_value = base_totals.get(drug, int(random.uniform(5e6, 5e8)))
        weights = [random.uniform(0.5, 1.8) for _ in INDIA_STATES]
        s = sum(weights)
        for i, st in enumerate(INDIA_STATES):
            share = weights[i] / s
            value = round(total_value * share * random.uniform(0.8, 1.2))
            units = int(value / random.uniform(3500, 9000))
            rows.append({
                "state": st,
                "drug": drug,
                "value_inr": value,
                "units": units,
                "period": f"{from_date}_to_{to_date}"
            })
    return pd.DataFrame(rows)

# -------------------------
# 3. Excel Report Builder
# -------------------------
def save_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Raw", index=False)
        agg = df.groupby(["state", "drug"]).agg(value_inr=("value_inr","sum"), units=("units","sum")).reset_index()
        agg.to_excel(writer, sheet_name="Aggregated", index=False)
        pivot = agg.pivot_table(index="state", columns="drug", values="value_inr", fill_value=0)
        pivot.to_excel(writer, sheet_name="Pivot_State_Drug")
    output.seek(0)
    return output

# -------------------------
# 4. Streamlit App
# -------------------------
st.set_page_config(page_title="Wegovy & Competitors Sales Dashboard", layout="wide")
st.title("📊 Wegovy & Competitors — Sales Analysis Dashboard (India)")

# Sidebar Filters
st.sidebar.header("Configuration")
drugs = st.sidebar.multiselect(
    "Select Drugs", ["Rybelsus","Mounjaro","Wegovy"], default=["Rybelsus","Mounjaro","Wegovy"]
)
from_date = st.sidebar.date_input("From Date", pd.to_datetime("2025-01-01"))
to_date = st.sidebar.date_input("To Date", pd.to_datetime("2025-08-31"))

# Generate Data
df = generate_mock_state_sales(drugs, str(from_date), str(to_date))

# Fetch Pharma Headlines
with st.spinner("Fetching latest pharma news…"):
    headlines = scrape_news_headlines([d.lower() for d in drugs], pages=1)
if not headlines.empty:
    st.subheader("📰 Latest Pharma News Mentions")
    st.dataframe(headlines.head(15))
else:
    st.info("No news found for selected drugs.")

# Download Excel Report
excel_file = save_to_excel(df)
st.download_button(label="📥 Download Sales Report (Excel)", data=excel_file, file_name="sales_report.xlsx")

# Aggregated Data
df_agg = df.groupby(["state","drug"]).agg(value_inr=("value_inr","sum"), units=("units","sum")).reset_index()

# Top N States Visualization
st.subheader("🏆 Top States by Drug Sales")
top_n = st.slider("Select Top N States", min_value=5, max_value=20, value=10)
for drug in drugs:
    d = df_agg[df_agg["drug"]==drug].sort_values("value_inr", ascending=False).head(top_n)
    fig = px.bar(d, x="state", y="value_inr", title=f"Top {top_n} States for {drug}", labels={"value_inr":"Sales (INR)"})
    st.plotly_chart(fig, use_container_width=True)

# Market Share
st.subheader("📈 Market Share Across India")
market_share = df_agg.groupby("drug").value_inr.sum().reset_index()
fig_pie = px.pie(market_share, names="drug", values="value_inr", title="Market Share by Drug")
st.plotly_chart(fig_pie, use_container_width=True)

# Heatmap
st.subheader("🌏 State vs Drug Sales Heatmap")
pivot = df_agg.pivot_table(index="state", columns="drug", values="value_inr", fill_value=0)
fig_heatmap = px.imshow(pivot.T, labels=dict(x="State", y="Drug", color="Sales INR"), aspect="auto", title="State vs Drug Sales")
st.plotly_chart(fig_heatmap, use_container_width=True)

# -------------------------
# 5. Useful Data Sources for Real Sales Comparisons
# -------------------------
st.markdown("### 📌 Data Sources for Real Drug Sales Comparisons")
st.markdown("""
- **IQVIA India** → [https://www.iqvia.com](https://www.iqvia.com/)
- **PharmaTrac Reports** → [https://pharma-trac.com](https://pharma-trac.com)
- **AIOCD AWACS** → [https://aiocdawacs.com](https://aiocdawacs.com)
- **Pharmarack** → [https://pharmarack.com](https://pharmarack.com)
- **NPPA (Drug Pricing Authority)** → [https://nppaindia.nic.in](https://nppaindia.nic.in)
- **Govt Open Data Portal** → [https://data.gov.in](https://data.gov.in)
""")
