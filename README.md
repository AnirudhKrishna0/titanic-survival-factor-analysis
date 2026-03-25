# Titanic Survival Factor Analysis

## Problem
What factors most strongly influenced survival on the Titanic?  
Was survival random, co-occurences?

------

## Approach
- Used Python (Pandas) for data analysis  
- Performed group-based comparisons across:
  - Gender
  - Passenger class
  - Fare
  - Embarkment location  
- Compared survival rates across combinations of features  

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

------

## Key Insight

Survival was **not random**.

It followed a clear prioritization hierarchy:
1. Gender (women and children first)
2. Passenger class
3. Secondary factors (location, fare within class) logistics may have provided a major edge for some passengers 

Even when controlling for class:
- Gender remained the dominant factor  
- Class influenced physical access to lifeboats  

------

## Conclusion

The highest probability of survival:
- Female
- 1st class passenger
- From the United States
- Embarked from Southampton 

When gender is excluded:
- 1st class passengers had the highest survival probability
  (Marginal rise in odds)
- From the United States
- Embarked from Southampton 

This suggests survival was driven primarily by **social hierarchy and evacuation policy**, rather than chance.

------

## Tools Used

- Python  
- Pandas

## Dataset

Dataset sourced from: https://matthew-brett.github.io/cfd2020/data/titanic.html
Credits to the creators for compiling the Titanic passenger data.
