"""
Customer Churn Analysis - Data Cleaning Script

Purpose:
    Read the original IBM Telco Customer Churn CSV, clean TotalCharges,
    run basic data-quality checks, and save the cleaned CSV.

Expected project structure:
    Customer_Churn_Analysis/
    ├── 01_Dataset/
    │   ├── Raw_Data/
    │   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
    │   └── Cleaned_Data/
    └── 03_Python/
        └── Scripts/
            └── data_cleaning.py

Requirement:
    pip install pandas
"""

from pathlib import Path
import pandas as pd


# Find the project root from this script's location.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_FILE = (
    PROJECT_ROOT
    / "01_Dataset"
    / "Raw_Data"
    / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

CLEANED_FOLDER = PROJECT_ROOT / "01_Dataset" / "Cleaned_Data"
CLEANED_FILE = CLEANED_FOLDER / "Telco_Customer_Churn_Cleaned.csv"


def main():
    # 1. Check that the original dataset exists.
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw dataset not found:\n{RAW_FILE}\n"
            "Please place the original CSV in 01_Dataset/Raw_Data/."
        )

    # 2. Load the dataset.
    df = pd.read_csv(RAW_FILE)

    print("========== ORIGINAL DATASET ==========")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # 3. Validate important columns before cleaning.
    required_columns = {"customerID", "TotalCharges", "Churn"}
    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        raise ValueError(
            "The dataset is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    # 4. Check duplicate records and duplicate customer IDs.
    duplicate_rows = int(df.duplicated().sum())
    duplicate_customer_ids = int(df["customerID"].duplicated().sum())

    # 5. Clean TotalCharges.
    # Some zero-tenure customers have whitespace-only TotalCharges values.
    # Convert whitespace to missing, then convert those missing values to 0.
    total_charges_as_text = df["TotalCharges"].astype("string").str.strip()
    blank_total_charges = int(total_charges_as_text.eq("").sum())

    df["TotalCharges"] = pd.to_numeric(
        total_charges_as_text.replace("", pd.NA),
        errors="coerce"
    ).fillna(0)

    # 6. Run final data-quality checks.
    missing_values = df.isna().sum()
    missing_customer_ids = int(df["customerID"].isna().sum())
    missing_total_charges = int(df["TotalCharges"].isna().sum())
    missing_churn = int(df["Churn"].isna().sum())
    zero_total_charges = int(df["TotalCharges"].eq(0).sum())

    # 7. Create the output folder and save the cleaned dataset.
    CLEANED_FOLDER.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEANED_FILE, index=False, encoding="utf-8-sig")

    # 8. Display a cleaning report.
    print("\n========== DATA-CLEANING REPORT ==========")
    print(f"Duplicate rows found: {duplicate_rows}")
    print(f"Duplicate customer IDs found: {duplicate_customer_ids}")
    print(f"Whitespace-only TotalCharges found: {blank_total_charges}")
    print(f"Missing customerID after cleaning: {missing_customer_ids}")
    print(f"Missing TotalCharges after cleaning: {missing_total_charges}")
    print(f"Missing Churn after cleaning: {missing_churn}")
    print(f"TotalCharges values equal to 0: {zero_total_charges}")

    print("\nMissing values by column:")
    print(missing_values.to_string())

    print("\n========== CLEANING COMPLETED ==========")
    print(f"Cleaned rows: {df.shape[0]}")
    print(f"Cleaned columns: {df.shape[1]}")
    print(f"Saved file:\n{CLEANED_FILE}")


if __name__ == "__main__":
    main()
