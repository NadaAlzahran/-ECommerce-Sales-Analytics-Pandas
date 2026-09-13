# 🛒 E-Commerce Sales Analytics (Pandas & Matplotlib)

An end-to-end Python data analysis pipeline designed to clean, transform, and analyze e-commerce sales records. This project extracts key date components, cleans monetary values, calculates business KPIs (Sales, Cost, Profit), performs categorical grouping, and visualizes customer demographics.

---

## 📌 Key Features

* **Datetime Feature Engineering:** Extracts year, month names, day names, day shortcuts, and quarterly periods from raw date records.
* **Data Cleaning & Type Conversion:** 
  * Removes currency symbols (`$`) and formatting commas (`,`).
  * Converts `Unit Price` and `Unit Cost` columns to numeric `float` types.
* **KPI Calculations:**
  * Computes `Total_Sales` ($Quantity \times Unit Price$).
  * Computes `Total_Cost` ($Quantity \times Unit Cost$).
  * Computes Net `Profit` ($Total\_Sales - Total\_Cost$).
* **Aggregation & Pivoting:** Grouped analysis by product categories and pivot tables summarizing overall financial performance.
* **Data Visualization:** Generates visual distributions (e.g., customer gender pie charts) using Matplotlib.
* **Advanced Multi-Condition Filtering:** Filters subset records based on country, age groups, and product categories.

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Pandas** — Data manipulation, transformation, and aggregation.
* **Matplotlib** — Data visualization.

---

## 📁 Repository Structure

```text
├── E-Commerce-Sales-Analytics-Pandas/
│   ├── E-Commerce Sales.csv   # Raw e-commerce dataset
│   ├── main.py               # Main Python processing & analysis script
│   ├── newfile.csv           # Cleaned dataset output
│   └── README.md             # Project documentation
