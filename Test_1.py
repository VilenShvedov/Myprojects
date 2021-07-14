import pandas as pd

df = pd.read_csv('devel//names.csv')

df.to_csv('names', index=False, header=None)
new_df = pd.read_csv('names', header=None)
pd.set_option('display.max_columns',4)
print(new_df)
print(new_df.columns[0][2])