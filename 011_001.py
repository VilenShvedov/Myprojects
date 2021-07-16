import pandas as pd

df = pd.read_csv('2019.csv')
'''print(df.iterrows())

for index, row in df.iterrows():
    print(index)
    print(row['Country or region'])
    print(type(row))'''

#print(df.loc[df['GDP per capita'] < 1])

#print(df.shape)
'''print(df.describe())
print(df.dtypes)
print(df.loc[0, 'GDP per capita'])
print(type(df.loc[0, 'GDP per capita']))'''

#print(df.sort_values(['Generosity', 'GDP per capita',],ascending=[0, 1]))
'''df['Total'] = df['GDP per capita'] + df['Generosity'] + df['Social support'] #Mq sozdali dop tablicu Total i sumirovali zna4enija treh index
df2 = df.drop(columns=['Total', 'GDP per capita'])
print(df2.shape) # koli4estvo kolonok i rjadov
print(df.shape)
'''
#print(df.loc[df['Country or region'].str.contains('ain')]) # iwet po ain v slovah
#print(df.loc[df['Country or region'].str.fullmatch('Estonia')]) # polnoe sovpadenie
#print(df.loc[df['Country or region'].str.startswith('A')]) # na4inaets na opredelenoie so4etanie simvolov
#print(df.loc[df['Country or region'].str.endswith('ia')])

#print(df.loc[df['GDP per capita'] > 1, 'Country or region'])
#print(df.loc[df['GDP per capita'] > 1, ['Country or region', 'GDP per capita', 'Overall rank']])
# Esli odint parametr to square skobki ne nuznq 30 stroka, esli mnogo to 31 stroka
print(df.sort_values(by ='Generosity'))

print(df.groupby('GDP per capita').sum())

