python
import numpy as np
import pandas as pd

# 1. Simulate a raw, messy dataset (Simulating real-world data collection issues)
np.random.seed(42)
n_rows = 1000

raw_data = {
    "Transaction_ID": range(10001, 10001 + n_rows),
    "Date": pd.date_range(start="2025-01-01", periods=n_rows, freq="H"),
    "Product_Category": np.random.choice(
        ["Electronics", "Apparel", "Home", None], size=n_rows, p=[0.4, 0.3, 0.2, 0.1]
    ),
    "Units_Sold": np.random.choice(
        [1, 2, 3, 4, 5, -99], size=n_rows, p=[0.5, 0.3, 0.1, 0.05, 0.03, 0.02]
    ), # -99 represents data entry errors
    "Revenue": np.random.uniform(15.0, 500.0, size=n_rows),
}

df = pd.DataFrame(raw_data)

# 2. Data Cleaning Pipeline (Pandas & NumPy)
print("--- Initial Data Summary ---")
print(df.isnull().sum())

# Handle Missing Categories using structural imputation
df["Product_Category"] = df["Product_Category"].fillna("Uncategorized")

# Clean anomalous numerical values (-99 errors) using NumPy
df["Units_Sold"] = np.where(df["Units_Sold"] < 0, np.nan, df["Units_Sold"])
df["Units_Sold"] = df["Units_Sold"].fillna(
    df["Units_Sold"].median()
) # Impute with median values

# Ensure correct data schemas
df["Units_Sold"] = df["Units_Sold"].astype(int)
df["Total_Sales_Value"] = df["Units_Sold"] * df["Revenue"]

# 3. Exploratory Data Analysis (EDA)
print("\n--- Cleaned Structural Metrics ---")
category_summary = (
    df.groupby("Product_Category")
    .agg(
        Total_Units=("Units_Sold", "sum"),
        Average_Revenue=("Revenue", "mean"),
        Gross_Sales=("Total_Sales_Value", "sum"),
    )
    .reset_index()
)

print(category_summary)

# Save cleaned output for Tableau ingestion
df.to_csv("cleaned_ecommerce_sales.csv", index=False)
print("\n[SUCCESS] Data pipeline executed
