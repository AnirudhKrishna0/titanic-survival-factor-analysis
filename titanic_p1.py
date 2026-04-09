
import pandas as pd

main=pd.read_csv(r"C:\Users\aniru\OneDrive\Desktop\week 2\week1\titanic_clean.csv")

#print(main.isnull().sum())

#main=main[(main["survived"]=="yes") & (main["gender"]=="female")].value_counts("class")
#main=main[(main["survived"]=="yes") & (main["gender"]=="male")].value_counts("class")

#main=main[(main["survived"]=="yes")].value_counts("country")
#main=main[(main["survived"]=="yes")].value_counts("embarked")

#main=main[(main["country"]=="United States")&(main["gender"]=="male")&(main["survived"]=="yes")].value_counts("embarked")
#main=main[(main["country"]=="United States")&(main["gender"]=="female")&(main["survived"]=="yes")].value_counts("embarked")

#main=main[(main["country"]=="United States")&(main["gender"]=="male")&(main["survived"]=="yes")&(main["embarked"]=="Southampton")].value_counts("class")
#main=main[(main["country"]=="United States")&(main["gender"]=="female")&(main["survived"]=="yes")&(main["embarked"]=="Southampton")].value_counts("class")

#main=main[(main["country"]=="United States")&(main["gender"]=="male")&(main["survived"]=="yes")&(main["embarked"]=="Cherbourg")].value_counts("class")
#main=main[(main["country"]=="United States")&(main["gender"]=="female")&(main["survived"]=="yes")&(main["embarked"]=="Cherbourg")].value_counts("class")


main["fare_diff"] = main["fare"] > main.groupby("class")["fare"].transform("mean")
#main=main[(main["survived"]=="yes")].value_counts("fare_diff")



main["title"]=main["name"].str.split(",").str[1].str.split(".").str[0].str.strip()

def person_standing(row):
    if row["age"]<14:
        return "child"
    else:
        return row["title"]

main["person_standing"]=main.apply(person_standing,axis=1)

#main=main[main["person_standing"].isin(["Miss","Mrs","child"])].groupby(["class", "person_standing"])["survived"].value_counts()

#main=main[main["person_standing"].isin(["Miss","Mrs","child"])].groupby(["class","person_standing"])["survived"].apply(lambda x: round((x=="yes").mean()*100))


# ===== LOGISTIC REGRESSION =====

# 1. Target 
y = (main["survived"] == "yes").astype(int)

# 2. Features 

X = main.drop(columns=["name","survived","country","title","fare"]) #using fare_diff instead of fare, and person_standing instead of title 

# 3. Convert text to no.
X = pd.get_dummies(X, drop_first=True)

# 4. Split data 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train 
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Acc
print("Accuracy:", model.score(X_test, y_test))

# 7. Feature weights 
importance = pd.Series(model.coef_[0], index=X.columns).sort_values()
print(importance)

# ===== END? =====

#print(main)
