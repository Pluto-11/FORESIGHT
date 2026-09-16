import pandas as pd
from pathlib import Path


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# Load raw data
# --------------------------------------------------

sku_master = pd.read_csv(RAW_DIR / "sku_master.csv")
sales_daily = pd.read_csv(RAW_DIR / "sales_daily.csv")
calendar = pd.read_csv(RAW_DIR / "calendar.csv")
inventory = pd.read_csv(RAW_DIR / "inventory_snapshots.csv")


# --------------------------------------------------
# Date conversions
# --------------------------------------------------

sales_daily["Date"] = pd.to_datetime(
    sales_daily["Date"]
)

calendar["date"] = pd.to_datetime(
    calendar["date"]
)

inventory["Snapshot_Date"] = pd.to_datetime(
    inventory["Snapshot_Date"]
)

sku_master["Launch_Date"] = pd.to_datetime(
    sku_master["Launch_Date"]
)


# --------------------------------------------------
# Clean calendar event fields
# --------------------------------------------------

calendar["holiday"] = calendar["holiday"].fillna("No Holiday")

calendar["promotion_event"] = calendar["promotion_event"].fillna(
    "No Promotion"
)


# --------------------------------------------------
# Clean string fields
# --------------------------------------------------

string_columns = [
    "SKU",
    "Product_Name",
    "Category",
    "Subcategory"
]

for column in string_columns:
    sku_master[column] = sku_master[column].str.strip()

sales_daily["SKU"] = sales_daily["SKU"].str.strip()
inventory["SKU"] = inventory["SKU"].str.strip()


# --------------------------------------------------
# Save processed datasets
# --------------------------------------------------

sku_master.to_csv(
    PROCESSED_DIR / "sku_master_clean.csv",
    index=False
)

sales_daily.to_csv(
    PROCESSED_DIR / "sales_daily_clean.csv",
    index=False
)

calendar.to_csv(
    PROCESSED_DIR / "calendar_clean.csv",
    index=False
)

inventory.to_csv(
    PROCESSED_DIR / "inventory_clean.csv",
    index=False
)


print("Data cleaning completed successfully.")
print(f"Processed files saved to: {PROCESSED_DIR}")