import pandas as pd

main=pd.read_csv("data in csvs/titanic_clean.csv")

#main=main[(main["survived"]=="yes") & (main["gender"]=="female")].value_counts("class")
#main=main[(main["survived"]=="yes") & (main["gender"]=="male")].value_counts("class")

#main=main[(main["survived"]=="yes")].value_counts("country")

#main=main[(main["country"]=="United States")&(main["gender"]=="male")&(main["survived"]=="yes")].value_counts("embarked")
#main=main[(main["country"]=="United States")&(main["gender"]=="female")&(main["survived"]=="yes")].value_counts("embarked")

#main=main[(main["country"]=="United States")&(main["gender"]=="male")&(main["survived"]=="yes")&(main["embarked"]=="Southampton")].value_counts("class")
#main=main[(main["country"]=="United States")&(main["gender"]=="female")&(main["survived"]=="yes")&(main["embarked"]=="Southampton")].value_counts("class")


print(main)

