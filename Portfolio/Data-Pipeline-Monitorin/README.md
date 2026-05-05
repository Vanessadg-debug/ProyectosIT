# Data-Pipeline-Monitoring & Marketing Analytics

## 🔗 Project Links
* **Interactive Dashboard:** [View Dashboard in Looker Studio](https://datastudio.google.com/s/kuYrGATk5pQ)
* **Technical Explanation (Video):** [Watch project walkthrough](https://drive.google.com/file/d/16l6hxJmyY8lbFAk6_XeNnyXIKh9iKpLJ/view?usp=drive_link)

## 📝 Technical Purpose
This project demonstrates the ability to structure, clean, and visualize dynamic data flows. The primary focus was ensuring **data integrity** and KPI accuracy by transforming raw data into a reliable, interactive monitoring tool.

## 🛠️ Tech Stack
* **Data Source:** Google Sheets (Structuring and normalization).
* **Visualization:** Looker Studio (Interactive dashboard).
* **Logic Layer:** Looker calculated fields for performance optimization.

## 🛡️ Data Quality & Validation
To ensure accurate reporting and prevent data corruption, the following quality rules were implemented:
* **Chronological Consistency:** Date format standardization to ensure time-series accuracy.
* **String Normalization:** Transformation of campaign names to prevent duplication due to case-sensitivity (e.g., "Campaña_A" vs. "campaña_a").
* **Record Integrity:** Validation of critical fields and Null Handling to prevent errors in automatic calculations.

## 📊 Metric Logic (KPIs)
The mathematical logic was implemented at the visualization layer to allow for dynamic and efficient granularity:
* **CTR (Click-Through Rate):** `SUM(Clicks) / SUM(Impressions)` — Validates ad effectiveness.
* **CPC (Cost Per Click):** `SUM(Investment) / SUM(Clicks)` — Measures spend efficiency.
* **CPM (Cost Per Mille):** `(SUM(Investment) / SUM(Impressions)) * 1000` — Analyzes reach cost.

## 🎯 Project Focus
This repository is not about visual design, but about **technical data validation and analysis**. It was developed as a **Quality Engineering (QA)** exercise to demonstrate skills in:
* Identifying and resolving database inconsistencies.
* Implementing robust business logic.
* Creating metric monitoring systems — core competencies for **QA Automation and Site Reliability Engineering (SRE)** roles.