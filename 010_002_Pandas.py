import pandas as pd

df = pd.read_csv('2019.csv', skiprows=1, header=None, nrows=5,
                 names=['Overall rank','Country or region','Score',
                        'GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices',
                        'Generosity','perceptions of corruption'])

print(df)
df.to_csv('new_csv1', index=False, header=None)
new_df = pd.read_csv('new_csv1', header=None)
print(new_df)
print(new_df.columns[0]) # Soderzit v sebe vse nazvanija stolbov tak ze mozno v square skobkah
#ukazqvat nomer stolba
print(type(new_df.columns))
df.to_csv('new_csv2.csv', columns=['Country or region', 'GDP per capita', 'Healthy life expectancy'], index=False)
#skipwors will skip some rows depends on ={number}
#pd.set_option - изменяет строку
#names указывает именна для столбов
#nrows
#pd.set_option('display.max_columns', 9) #отоброжает максиммальное кол-во столбиков
#pd.set_option('display.max_rows',156)     #отоброжает максимальное кол-во строк
#index параметр который сохраняет или не сохраняет index,по умолчанию тру