# 📞 Customer Call List - Data Cleaning Pipeline

## 🎯 Project Overview
This sub-project focuses on cleaning and standardizing an unformatted and noisy customer call list Excel dataset to prepare it for outbound calling campaigns and analytics.

---

## ⚠️ Data Quality Issues Identified
The raw dataset contains multiple common real-world data quality problems:
1. **Duplicate Entries**: Duplicate customer rows with identical information.
2. **Malformed Phone Numbers**: Inconsistent formats including dashes, slashes, whitespace, and special characters.
3. **Dirty Text Fields**: Unwanted numbers/symbols in names (e.g. `_...`, `123/Smith`).
4. **Unparsed Address Fields**: Addresses combining Street, State, and Zip Code in single unindexed strings.
5. **Inconsistent Categorical Values**: Values like `Y`/`Yes`/`N`/`No`/`N/a`/`NaN` in boolean columns (`Paying Customer`, `Do_Not_Contact`).
6. **Redundant Columns**: Columns containing irrelevant or placeholder data (e.g., `Not_Useful_Column`).

---

## 🛠️ Cleaning Pipeline & Transformation Steps
- **Step 1 - De-duplication**: `drop_duplicates()` on customer records.
- **Step 2 - Column Pruning**: Dropping non-value-adding metadata columns.
- **Step 3 - String Cleaning**: Stripping non-alphabetical noise from customer last names.
- **Step 4 - Phone Number Standardization**: Regex parsing `\D` to extract 10 digits and reformat into `XXX-XXX-XXXX`.
- **Step 5 - Address Parsing**: Splitting compound strings into `Street_Address`, `State`, and `Zip_Code`.
- **Step 6 - Categorical Normalization**: Mapping boolean flags to uniform `Yes` / `No` strings.
- **Step 7 - Business Rule Filtering**: Filtering out customers flagged as `Do_Not_Contact == 'Yes'` or with missing phone numbers.

---

## 📁 Directory Structure
```text
Customer_call_list/
├── data/
│   ├── raw/
│   │   └── Customer Call List.xlsx
│   └── processed/
│       └── Customer_Call_List_Cleaned.csv
├── notebooks/
│   └── clean1.ipynb
├── src/
│   └── clean_customer_data.py
└── README.md
```

---

## 🚀 How to Run

### 1. Via Python Script:
```bash
python projects/Customer_call_list/src/clean_customer_data.py
```

### 2. Via Jupyter Notebook:
Open and execute all cells in [clean1.ipynb](file:///projects/Customer_call_list/notebooks/clean1.ipynb).