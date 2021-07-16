import pandas as pd

df = pd.read_csv('1.csv')
print(df.groupby('town').idxmax().sort_values('num'))
print(df.loc[4, 'num'])