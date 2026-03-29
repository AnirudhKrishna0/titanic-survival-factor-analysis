
import pandas as pd

main=pd.read_csv("titanic_clean.csv")

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

'''
main["fare_diff"] = main["fare"] > main.groupby("class")["fare"].transform("mean")
main=main[(main["survived"]=="yes")].value_counts("fare_diff")

'''


main["title"]=main["name"].str.split(",").str[1].str.split(".").str[0].str.strip()

def person_standing(row):
    if row["age"]<14:
        return "child"
    else:
        return row["title"]

main["person_standing"]=main.apply(person_standing,axis=1)

#main=main[main["person_standing"].isin(["Miss","Mrs","child"])].groupby(["class", "person_standing"])["survived"].value_counts()

main=main[main["person_standing"].isin(["Miss","Mrs","child"])].groupby(["class","person_standing"])["survived"].apply(lambda x: round((x=="yes").mean()*100))

print(main)

