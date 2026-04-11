# Titanic Survival Factor Analysis

This project focuses on understanding *why* passengers survived, not just predicting survival.

The goal is to clearly separate:
- Observed patterns in the data (EDA)
- Learned relationships from a machine learning model

---

## Problem

What factors most strongly influenced survival on the Titanic?

Was survival random, or driven by identifiable patterns?

---

## Approach

- Data Cleaning using Pandas  
- Exploratory Data Analysis (EDA) using percentage-based comparisons  
- Feature Engineering to extract meaningful signals  
- Logistic Regression as an interpretable baseline model  

---

## Exploratory Data Analysis (EDA)

EDA was performed using **percentage-based survival rates**, not raw counts.

### Key Patterns

- Women and children had significantly higher survival rates  
- Passenger class strongly influenced survival outcomes  
- Third class showed sharply lower survival, even among priority groups  

> EDA identifies observed patterns in the data but does not quantify predictive strength.

---

## Interaction Insight: Class × Passenger Type

Survival was not determined by a single factor.

- Women and children had higher survival overall  
- However, this advantage was significantly reduced in 3rd class  

Example:
- 1st/2nd class women & children → ~85–100% survival  
- 3rd class → ~37–51% survival  

> This suggests socio-economic constraints influenced access to lifeboats.

---

## Feature Engineering

- Title extraction → proxy for social status  
- person_standing → behavioral grouping  
- fare_diff → relative pricing signal  
- Removed raw name → reduces noise  

---

## Model: Logistic Regression

- Binary classification problem  
- Chosen for interpretability  

### Evaluation

- Baseline Accuracy: **61%**  
- Model Accuracy: **~78%**

> The model improves significantly over baseline, indicating meaningful learning.

---

## Model Interpretation

- Male → strong negative impact  
- 3rd class → strongest negative factor  
- Female-related features → positive impact  
- Age → minor negative effect  

> Coefficients show direction and strength, not probabilities.

---

## Key Insights

- Survival was not random  
- Gender is the primary driver  
- Class acts as a strong constraint  
- Class can override gender advantage in lower classes  
- Access to lifeboats likely influenced outcomes  

---

## Limitations

- Small dataset  
- Linear model assumption  
- No interaction terms explicitly modeled  
- No time/context data  

---

## Improvements

- Add interaction terms  
- Try tree-based models  
- Add more contextual features  

---

## Conclusion

Survival followed a clear hierarchy:

1. Gender  
2. Passenger class  
3. Secondary factors  

The model confirms survival was driven by structured social dynamics, not randomness.

---

## Tools Used

- Python  
- Pandas  
- Scikit-learn  

---

## Dataset

https://matthew-brett.github.io/cfd2020/data/titanic.html  

---

## How to Run

pip install pandas scikit-learn  

python titanic_p1.py