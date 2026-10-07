# E-Commerce Sales & Inventory Forecasting Pipeline

## 📊 Business Overview
In retail operations, unexpected stockouts cause lost revenue, while overstocking chains down vital business capital. This project builds an automated data pipeline using **Python, Pandas, and NumPy** to ingest raw transactional sales data, systematically isolate operational anomalies, execute programmatic data cleaning, and calculate high-level performance metrics necessary for supply chain forecasting.

## 🛠️ Technical Tech Stack & Libraries
* **Language:** Python 3.10+
* **Data Manipulation:** Pandas (Dataframe restructuring, grouping, structural imputation)
* **Numerical Processing:** NumPy (Array manipulation, programmatic error flags, conditional vector masking)
* **Execution Environment:** Jupyter Notebook / Command Line Interface (CLI)

## 🔑 Core Features & Data Cleaning Architecture
* **Structural Data Imputation:** Programmatically captured missing structural categorical keys (`Product_Category`) and updated null strings with explicit classification metrics to prevent database pipeline errors.
* **Algorithmic Outlier Mitigation:** Leveraged NumPy vectorized conditions to isolate bad numerical records (e.g., negative inventory data entry mistakes) and safely adjusted values using data-driven median imputation.
* **Operational Feature Engineering:** Transformed base transactional metrics into structural analytical variables (`Total_Sales_Value`) to provide clear visual key performance indicators (KPIs).

## 🚀 How To Run The Pipeline
1. Clone this repository to your local workspace.
2. Install the required dependencies: `pip install pandas numpy`
3. Execute the automated script file: `python sales_forecasting.py`
4. The script cleans the target dataset and outputs a pristine, reporting-ready file: `cleaned_ecommerce_sales.csv`.
