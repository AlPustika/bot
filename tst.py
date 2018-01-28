import pandas as pd

df = pd.read_csv('studios.csv')
print(type(df.Country))
all_cntry = pd.unique(df.Country)
print(type(all_cntry))
cnt = 'Poland'
city = pd.unique(df[df.Country == cnt][['City']].squeeze())
print(type(city),city)