# 🧹 Data Cleaning & Preprocessing Projects

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A curated collection of end-to-end data cleaning pipelines, exploratory data analysis (EDA), and machine learning preprocessing projects implemented in Python, Pandas, and Scikit-Learn.

---

## 📂 Repository Structure

```text
Data-Cleaning-Projects/
├── .github/
│   └── workflows/
│       └── data_pipeline.yml          # Automated CI pipeline & testing
├── projects/
│   ├── Customer_call_list/             # Project 1: Unstructured Customer Contact Cleaning
│   │   ├── data/
│   │   │   ├── raw/                   # Original unformatted Excel dataset
│   │   │   └── processed/             # Cleaned ready-for-contact dataset
│   │   ├── notebooks/
│   │   │   └── clean1.ipynb           # Step-by-step interactive notebook
│   │   ├── src/
│   │   │   └── clean_customer_data.py # Automated Python cleaning pipeline
│   │   └── README.md
│   │
│   └── Salary_Linear_Regression/       # Project 2: Salary Prediction & Regression Modeling
│       ├── data/
│       │   └── raw/                   # Raw Experience & Salary data
│       ├── notebooks/
│       │   └── linear-regression-salary-dataset.ipynb
│       ├── src/
│       │   └── train_predict.py       # ML Training, evaluation & inference script
│       └── README.md
│
├── utils/                             # Shared data cleaning and validation helpers
│   ├── __init__.py
│   ├── text_cleaner.py                # Regex and string normalization helpers
│   └── data_profiler.py               # Missing values & DataFrame profiling
│
├── main.py                            # Master orchestrator for running all pipelines
├── requirements.txt                   # Project dependencies
├── .gitignore                         # Git exclusion rules
└── README.md                          # Repository documentation
```

---

## 🚀 Projects Overview

| # | Project Name | Key Techniques & Tools | Deliverables |
|---|--------------|------------------------|--------------|
| **01** | [Customer Call List](projects/Customer_call_list/) | Regex, Missing Value Imputation, String Parsing, De-duplication | Clean CSV, Automated Pipeline Script |
| **02** | [Salary Linear Regression](projects/Salary_Linear_Regression/) | Simple Linear Regression, Train/Test Split, $R^2$ Evaluation, OLS | Trained Model, Predictive Script |

---

## ⚙️ Installation & Setup

### 1. Clone the repository:
```bash
git clone https://github.com/doanquangminh14/Data-Cleaning-Projects.git
cd Data-Cleaning-Projects
```

### 2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages:
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Projects

### Run All Pipelines at Once:
```bash
python main.py
```

### Run Individual Pipelines:
```bash
# Project 1: Customer Call List
python projects/Customer_call_list/src/clean_customer_data.py

# Project 2: Salary Linear Regression
python projects/Salary_Linear_Regression/src/train_predict.py
```

---

## 👤 Author
- **GitHub**: [@doanquangminh14](https://github.com/doanquangminh14)

---

## 📜 License
This repository is open-sourced under the [MIT License](LICENSE).