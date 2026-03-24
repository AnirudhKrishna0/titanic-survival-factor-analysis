import pandas as pd

data=(pd.read_csv("C:\\Users\\aniru\\OneDrive\\Desktop\\week1\\data in csvs\\customers-100.csv",index_col=0))
print(data["Email"].value_counts())