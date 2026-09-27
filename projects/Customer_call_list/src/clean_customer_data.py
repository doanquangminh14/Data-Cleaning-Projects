"""
Customer Call List Data Cleaning Pipeline
=========================================
This script automates the end-to-end data cleaning workflow for the customer call list:
1. Removal of duplicate records
2. Cleaning and normalization of text fields (First/Last Names, Address)
3. Standardizing phone numbers into uniform formatting
4. Normalizing boolean columns (Paying Customer, Do_Not_Contact)
5. Handling missing / invalid values (N/a, NaN, nulls)
6. Exporting cleaned, production-ready dataset
"""

import os
import re
import pandas as pd


def clean_customer_call_list(
    input_path: str = "data/raw/Customer Call List.xlsx",
    output_path: str = "data/processed/Customer_Call_List_Cleaned.csv"
) -> pd.DataFrame:
    """
    Load raw customer call list and perform thorough data cleaning.
    """
    if not os.path.exists(input_path):
        # Allow running from project subfolder or repo root
        base_dir = os.path.dirname(os.path.abspath(__file__))
        alt_input_path = os.path.join(base_dir, "..", input_path)
        if os.path.exists(alt_input_path):
            input_path = alt_input_path
            output_path = os.path.join(base_dir, "..", output_path)

    print(f"[*] Reading raw customer data from: {input_path}")
    df = pd.read_excel(input_path)
    initial_rows = len(df)

    # 1. Drop duplicate records
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"[-] Dropped {initial_rows - len(df)} duplicate rows")

    # 2. Drop unneeded columns if present
    if "Not_Useful_Column" in df.columns:
        df = df.drop(columns=["Not_Useful_Column"])

    # 3. Clean string columns (strip unwanted special characters)
    if "Last_Name" in df.columns:
        df["Last_Name"] = df["Last_Name"].astype(str).str.strip("1234567890/_.")
        df["Last_Name"] = df["Last_Name"].replace(["nan", "NaN", "None", ""], None)

    # 4. Standardize Phone Numbers (digits only, formatted as XXX-XXX-XXXX)
    if "Phone_Number" in df.columns:
        df["Phone_Number"] = df["Phone_Number"].astype(str)
        df["Phone_Number"] = df["Phone_Number"].apply(lambda x: re.sub(r"[^0-9]", "", x))
        
        def format_phone(p):
            if len(p) == 10:
                return f"{p[:3]}-{p[3:6]}-{p[6:]}"
            return None
        
        df["Phone_Number"] = df["Phone_Number"].apply(format_phone)

    # 5. Split Address into Street_Address, State, Zip_Code if comma-separated
    if "Address" in df.columns:
        split_address = df["Address"].astype(str).str.split(",", expand=True)
        if split_address.shape[1] >= 3:
            df["Street_Address"] = split_address[0].str.strip()
            df["State"] = split_address[1].str.strip()
            df["Zip_Code"] = split_address[2].str.strip()
            df = df.drop(columns=["Address"])

    # 6. Normalize Boolean / Category Columns: Paying Customer, Do_Not_Contact
    bool_mappings = {
        "Y": "Yes",
        "Yes": "Yes",
        "N": "No",
        "No": "No"
    }
    
    if "Paying Customer" in df.columns:
        df["Paying Customer"] = df["Paying Customer"].astype(str).str.strip().map(bool_mappings)

    if "Do_Not_Contact" in df.columns:
        df["Do_Not_Contact"] = df["Do_Not_Contact"].astype(str).str.strip().map(bool_mappings)

    # 7. Replace placeholder strings with standard missing value representations
    df = df.replace({"N/a": None, "nan": None, "NaN": None, "None": None, "": None})

    # 8. Filter out customers with Do_Not_Contact == 'Yes' or missing phone numbers
    if "Do_Not_Contact" in df.columns:
        df = df[df["Do_Not_Contact"] != "Yes"]
    if "Phone_Number" in df.columns:
        df = df[df["Phone_Number"].notna()]

    df = df.reset_index(drop=True)

    # Ensure output directory exists and save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[+] Successfully exported {len(df)} clean records to: {output_path}")

    return df


if __name__ == "__main__":
    clean_customer_call_list()
