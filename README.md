### Update Ver 5 : Titanic Survival Factor Analysis 

Refined the analysis by converting raw survival counts into percentage-based survival rates across class on certain social groups.

Key finding: While women and children had the highest survival rates overall, class significantly influenced outcomes.
First and second class passengers showed extremely high survival rates (85–100%), whereas third class survival dropped sharply (37–51%), indicating that class constraints impacted even priority groups like children.

Added Logistic Regression model to validate result 

Used fare_diff instead of fare, and person_standing instead of title for better scaling feature

## Problem

What factors most strongly influenced survival on the Titanic?  
Was survival random, co-occurrences?

------

## Approach

- Used Python (Pandas) for data analysis  
- Performed group-based comparisons across:
  - Gender
  - Passenger class
  - Fare
  - Embarkment location  
- Compared survival rates across combinations of features  
- Used Logistic Regression as a baseline model because:
  - Works well for binary classification problems
  - Provides interpretable feature importance through learned weights
  
------

## Key Findings

- **Gender had the strongest influence**  
  - Females had significantly higher survival rates than males  

- **Passenger class was the second strongest factor**  
  - 1st class passengers had much higher survival rates than 2nd and 3rd  

- **Fare within the same class had limited impact**  
  - Paying more within a class did not significantly increase survival  
  - Class itself dominated survival outcomes  

- **Embarkation location correlated with class distribution**  
  - Most 1st class passengers boarded at Cherbourg and Southampton  
  - 3rd class passengers were more concentrated at other ports  

- **Country-level survival reflects passenger distribution**  
  - Most survivors were from the US and England  
  - This aligns with the majority composition of passengers, not necessarily higher survival advantage  

- **Class modifies survival within each group**
  - Survival on the Titanic was primarily driven by gender and age (women and children first), but class significantly influenced outcomes within these groups.
  - Women and children had the highest survival rates overall, but class had a decisive impact—first and second class passengers had extremely high survival (85–100%), while third class saw a sharp drop (around 37–51%), indicating that class significantly constrained the ‘women and children first’ principle.
  - Notably, only 37% of third-class children survived, showing that class could override even the highest-priority survival group.

-------

## Limitations

- Logistic Regression assumes linear relationships between features and outcome
- May fail to capture complex interactions between variables
- Dataset size is limited can affect generalization

------

## Key Insight

Survival was **not random**.

This analysis is based on counts, not normalized survival rates, which may slightly bias interpretation.

It followed a clear prioritization hierarchy:
1. Gender (women and children first)
2. Passenger class
3. Secondary factors (location, fare within class) logistics may have provided a major edge for a very few passengers 
4. Miss/Mrs survival >> men

Even when controlling for class:
- Gender remained the dominant factor  
- Class influenced physical access to lifeboats  

Applied Logistic Regression using an 80/20 train-test split to evaluate performance on unseen data.
  - Gender, age , class, Person_Standing, Embarked and Fare were used as the main features
  - achieved a 79% accuracy using logistic regression 
  - used fare_diff instead of fare, and person_standing instead of title 
  - Removing fare slightly reduced model accuracy, suggesting it still contains some predictive signal. However, its impact was limited compared to gender and class.

  ### 📊 Model Interpretation (Top Factors)
    - Gender (male) → strong negative impact on survival  
    - 3rd Class → strong negative impact  
    - Titles (Mr, Mrs, Miss) → strong social indicators  
    - Age → minor influence negatively 

------

## Conclusion

Survival on the Titanic was not random.

The strongest factors were:
1. Gender
2. Passenger class

Logistic regression confirmed that social hierarchy and evacuation policies played a dominant role in survival outcomes.

------

## Tools Used

- Python  
- Pandas

## Dataset

Dataset sourced from: https://matthew-brett.github.io/cfd2020/data/titanic.html
Credits to the creators for compiling the Titanic passenger data.
