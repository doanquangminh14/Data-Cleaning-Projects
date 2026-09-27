# 📈 Salary Prediction - Simple Linear Regression

## 🎯 Overview
This project models the mathematical relationship between an employee's **Years of Experience** and their annual **Salary** using Simple Linear Regression ($y = mx + c$).

---

## 📊 Dataset Information
- **Source**: `Salary_Data.csv`
- **Features**:
  - `YearsExperience` (Float): Total years of professional work experience.
  - `Salary` (Float/Integer): Annual salary compensation ($ USD).
- **Size**: 30 observations.

---

## 🔬 Model Formulation
The Ordinary Least Squares (OLS) Linear Regression model fits the line:
$$\text{Salary} = \beta_1 \cdot (\text{YearsExperience}) + \beta_0$$

Where:
- $\beta_1$ (Slope): Represents the average salary increase per additional year of experience (~$9,423/yr).
- $\beta_0$ (Intercept): Baseline starting salary estimate (~$25,321).

### Evaluation Metrics
- **$R^2$ Score**: $> 0.90$ (High explanatory variance)
- **RMSE**: Root Mean Squared Error indicating low prediction variance
- **MAE**: Mean Absolute Error

---

## 📁 Directory Structure
```text
Salary_Linear_Regression/
├── data/
│   └── raw/
│       └── Salary_Data.csv
├── notebooks/
│   └── linear-regression-salary-dataset.ipynb
├── src/
│   └── train_predict.py
└── README.md
```

---

## 🚀 How to Run

### 1. Run ML Training & Inference Script:
```bash
python projects/Salary_Linear_Regression/src/train_predict.py
```

### 2. Run Jupyter Interactive Notebook:
Open and execute [linear-regression-salary-dataset.ipynb](file:///projects/Salary_Linear_Regression/notebooks/linear-regression-salary-dataset.ipynb).
