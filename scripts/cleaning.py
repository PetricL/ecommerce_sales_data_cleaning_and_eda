import pandas as pd

# Load the dataset
df = pd.read_csv("messy_ecommerce_sales_data.csv")

# Removing spaces in column names
df.columns = df.columns.str.strip() 

# Clean Quantity column
df["Quantity_Numeric"] = pd.to_numeric(df["Quantity"], errors="coerce")
df = df[df["Quantity_Numeric"] >= 0]
df = df.drop(columns=["Quantity"])
df = df.rename(columns={"Quantity_Numeric": "Quantity"})
df = df.reset_index(drop=True)

# Clean Price column
df["Price_Clean"] = (
    df["Price"]
    .astype(str)
    .str.strip()
    .str.replace("$", "", regex=False)
    .str.replace("€", "", regex=False)
    .str.replace("kr", "", regex=False)
)
df["Price_Numeric"] = pd.to_numeric(df["Price_Clean"], errors="coerce")
df = df[df["Price_Numeric"] >= 0]
df = df.drop(columns=["Price", "Price_Clean"])
df = df.rename(columns={"Price_Numeric": "Price"})
df = df.reset_index(drop=True)

# Recalculate Total column
df["Total"] = df["Quantity"] * df["Price"]

# Clean Order_Date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df.loc[df["Order_ID"] == "ORD-77417", "Order_Date"] = "2023-01-05"
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Clean Category column
df["Category"] = (
    df["Category"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({"electronic": "electronics", "electonics": "electronics"})
    .str.capitalize()
    .fillna("Unknown")
)

# Clean text columns
df["Customer_Name"] = df["Customer_Name"].str.strip()
df["Payment_Method"] = df["Payment_Method"].str.strip()
df["Status"] = df["Status"].str.strip()
df["Order_ID"] = df["Order_ID"].str.strip()

# Clean Product column
df["Product"] = (
    df["Product"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({"shoes": "Shoes"})
    .str.title()
)

# Remove duplicates
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print(f"Duplicates removed: {before - after}")

# Save cleaned dataset
df.to_csv("cleaned_ecommerce_sales_data.csv", index=False)

print("Dataset successfully cleaned and saved as cleaned_ecommerce_sales_data.csv")
print(df.isna().sum())