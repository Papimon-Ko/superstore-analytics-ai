# Superstore Sales Analytics — Portfolio Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C9BE8)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)

An end-to-end data analytics project built on the Sample Superstore dataset — covering data cleaning, SQL analysis, interactive dashboards, and AI-generated insights. Built as a portfolio piece for a Data Analyst role.

---

## Project Overview

The Superstore dataset contains **9,994 sales transactions** from a US retail company spanning **4 years (2014–2017)** across 3 product categories, 4 regions, and 3 customer segments.

**Core question answered:** *Where is the business growing, and where is it quietly losing money?*

Key findings from the analysis:
- Revenue grew ~84% from 2014 to 2017, but **Q4 accounts for ~34% of annual sales** — a significant seasonal concentration risk
- **~30% of all orders are unprofitable**, almost entirely caused by discounts above 30%
- **Furniture's profit margin is only ~2.5%** despite generating $742K in revenue — the worst category by efficiency
- The **West region leads** on both revenue and profitability; Central has the worst combination of low sales and low margin
- A discount policy cap at 20% would be the single highest-impact operational change available

---

## Repository Structure

```
superstore-analytics-ai/
│
├── superstore_eda_report.ipynb   ← Main portfolio notebook (start here)
│
├── 1_data_cleaning.ipynb         ← Phase 1: Data cleaning & preprocessing
├── 2_sql_analysis.ipynb          ← Phase 2: SQL queries via SQLite
├── 3_superstore_dashboard.pbix   ← Phase 3: Interactive Power BI dashboard
├── 4_ai_insights.ipynb           ← Phase 4: AI-generated insights via GPT
│
├── data/
│   └── README.md                 ← Instructions for downloading the dataset
│
├── requirements.txt              ← Python dependencies
├── .gitignore
└── README.md
```

---

## Notebooks

| Notebook | Description | Tools |
|----------|-------------|-------|
| [`superstore_eda_report.ipynb`](superstore_eda_report.ipynb) | Full EDA pipeline: load, clean, visualise, and report findings as a business analyst would | pandas, matplotlib, seaborn |
| [`1_data_cleaning.ipynb`](1_data_cleaning.ipynb) | Initial data profiling, null handling, type fixes, and export of cleaned CSV | pandas, numpy |
| [`2_sql_analysis.ipynb`](2_sql_analysis.ipynb) | Business queries using SQL (SQLite) — revenue by segment, top states, shipping analysis | sqlite3, pandas |
| [`4_ai_insights.ipynb`](4_ai_insights.ipynb) | GPT-4o-mini generates plain-English business insights from aggregated sales data | OpenAI API |

---

## Main Notebook — `superstore_eda_report.ipynb`

The main portfolio notebook is structured in 4 sections:

### Section 1 — Load & Explore
Profile the raw dataset: shape, column types, null counts, descriptive statistics, categorical distributions, and date range validation.

### Section 2 — Data Cleaning
Fix date types, cast Postal Code to string, remove duplicates, validate discount range, engineer new features (`Shipping_Days`, `Profit_Margin`, `Order_Year`, `Order_Month`, `Order_Quarter`), and flag outliers using the IQR method.

### Section 3 — EDA & Visualisation
Five business-focused charts:

| # | Chart | Business Question |
|---|-------|------------------|
| 3.1 | Monthly Sales Trend (overall + YoY overlay) | Is revenue growing? When are peak seasons? |
| 3.2 | Sales & Profit by Category (grouped bar + margin) | Which categories are efficient vs. just high-volume? |
| 3.3 | Top 10 & Bottom 10 Products by Profit | Which products drive vs. destroy value? |
| 3.4 | Regional Performance (sales, profit, margin) | Which regions outperform, and why might others lag? |
| 3.5 | Discount vs. Profit (scatter + violin by bucket) | Where is the discount tipping point into losses? |

### Section 4 — Summary Report
Business-style written report with 5 findings, 5 ranked recommendations, and an honest data limitations section.

---

## Setup & Running

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/superstore-analytics-ai.git
cd superstore-analytics-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
The raw data file is not included in this repository (see [`data/README.md`](data/README.md) for instructions).  
Place the downloaded file at: `data/Sample - Superstore.csv`

### 4. Run the notebooks
```bash
jupyter notebook
```
Open `superstore_eda_report.ipynb` and run all cells (`Kernel → Restart & Run All`).

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| pandas | Data manipulation |
| numpy | Numerical operations |
| matplotlib / seaborn | Visualisation |
| SQLite / sqlite3 | SQL analysis |
| Power BI Desktop | Interactive dashboard |
| OpenAI API (GPT-4o-mini) | AI-generated insights |
| Jupyter Notebook | Interactive development environment |

---

## Author

**Papimon Kongnark**  
Year 3 Data Science Student  
[GitHub](https://github.com/Papimon-Ko) · [LinkedIn](www.linkedin.com/in/papimon-kongnark-72738126b)
