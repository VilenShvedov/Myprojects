import pandas as pd
import json

with open('sample3.json', 'r', encoding='utf8') as file:
    data = json.load(file)



df = pd.DataFrame(data['people'])
print(df)
print(type(df))
df.to_csv('new_csv1')
