import numpy as np
import pandas as pd
import random

# -----------------------------
# Sales Data Generator
# -----------------------------
def generate_sales_data(n_rows=100000, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    regions = ["North", "South", "East", "West"]
    product_categories = ["Electronics", "Furniture", "Clothing", "Sports"]

    df = pd.DataFrame({
        "Month": np.random.choice(months, n_rows),
        "Region": np.random.choice(regions, n_rows),
        "Product_Category": np.random.choice(product_categories, n_rows),
        "Revenue": np.random.randint(50000, 250000, n_rows).astype(float),
        "Units_Sold": np.random.randint(50, 800, n_rows).astype(float),
        "Marketing_Spend": np.random.randint(5000, 100000, n_rows).astype(float),
    })

    # Add realistic noise
    df["Revenue"] += np.random.normal(0, 5000, n_rows)
    df["Units_Sold"] += np.random.normal(0, 10, n_rows)

    # Target
    df["Monthly_Sales"] = (
        df["Revenue"] * 0.8 +
        df["Marketing_Spend"] * 1.5 +
        np.random.normal(0, 10000, n_rows)
    )

    df["Hit_Target"] = np.where(df["Monthly_Sales"] > 150000, "Yes", "No")

    # Missing values
    for col in ["Revenue", "Units_Sold", "Marketing_Spend"]:
        df.loc[df.sample(frac=0.05).index, col] = np.nan

    return df


# -----------------------------
# Customer Churn Data Generator
# -----------------------------
def generate_churn_data(n_rows=100000, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    tenure = np.random.randint(1, 72, n_rows)
    monthly_charges = np.random.uniform(20, 120, n_rows)
    total_charges = tenure * monthly_charges + np.random.normal(0, 50, n_rows)

    df = pd.DataFrame({
        "CustomerID": np.arange(1, n_rows + 1),
        "Age": np.random.randint(18, 70, n_rows),
        "Gender": np.random.choice(["Male", "Female"], n_rows),
        "Contract_Type": np.random.choice(["Month-to-Month", "1 Year", "2 Year"], n_rows),
        "Tenure_Months": tenure,
        "Monthly_Charges": monthly_charges,
        "Total_Charges": total_charges
    })

    # Churn logic
    churn_prob = (
        (monthly_charges > 90).astype(int) * 0.5 +
        (df["Contract_Type"] == "Month-to-Month").astype(int) * 0.4 +
        (tenure < 12).astype(int) * 0.3 +
        np.random.uniform(0, 0.2, n_rows)
    )

    df["Churn"] = np.where(churn_prob > 0.6, "Yes", "No")

    # Missing values
    df.loc[df.sample(frac=0.03).index, "Total_Charges"] = np.nan

    return df


# -----------------------------
# Marketing Campaign Data Generator
# -----------------------------
def generate_marketing_data(n_rows=100000, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    channels = ["Email", "Social Media", "TV", "Radio", "Google Ads"]
    products = ["Electronics", "Fashion", "Grocery", "Appliances"]

    df = pd.DataFrame({
        "Customer_Age": np.random.randint(18, 65, n_rows),
        "Income": np.random.randint(15000, 200000, n_rows),
        "Marketing_Channel": np.random.choice(channels, n_rows),
        "Product": np.random.choice(products, n_rows),
        "Ad_Spend": np.random.randint(500, 50000, n_rows),
        "Clicks": np.random.randint(0, 1500, n_rows),
        "Impressions": np.random.randint(1000, 100000, n_rows),
    })

    df["CTR"] = df["Clicks"] / df["Impressions"]

    # Target: Conversion Yes/No
    conversion_prob = (
        (df["Ad_Spend"] > 20000).astype(int) * 0.4 +
        (df["Clicks"] > 200).astype(int) * 0.3 +
        (df["CTR"] > 0.02).astype(int) * 0.3 +
        np.random.uniform(0, 0.1, n_rows)
    )

    df["Converted"] = np.where(conversion_prob > 0.5, "Yes", "No")

    # Missing values
    df.loc[df.sample(frac=0.03).index, "Clicks"] = np.nan

    return df


# -----------------------------
# Generate All 3 CSV files
# -----------------------------
sales_df = generate_sales_data()
sales_df.to_csv("sales_data.csv", index=False)

churn_df = generate_churn_data()
churn_df.to_csv("customer_churn.csv", index=False)

marketing_df = generate_marketing_data()
marketing_df.to_csv("marketing_data.csv", index=False)

print("Generated:")
print(" - sales_data.csv")
print(" - customer_churn.csv")
print(" - marketing_data.csv")
