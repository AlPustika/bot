import pandas as pd

df = pd.read_csv('studios.csv')

all_cntry = pd.unique(df.Country)
print(all_cntry)