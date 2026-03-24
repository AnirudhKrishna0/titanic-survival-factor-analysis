import pandas as pd
print(pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},index=['2017 Sales',"2018 Sales"]))
print(pd.Series({"A": 10, "B": 20, "C": 30},name="my series"))