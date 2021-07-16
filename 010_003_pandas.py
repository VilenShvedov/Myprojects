import pandas as pd

df = pd.read_csv('2019.csv')
number = 0

while number < df.shape[0]:
    if df.loc[number, 'Perceptions of corruption'] < 1:
        print(df.loc[number, 'Country or region'], df.loc[number, 'Perceptions of corruption'],
              df.loc[number, 'GDP per capita'])
    number +=1







'''print(df.iloc[1,2])
print(df.loc[[1,3], ['name', 'email']])

print(df.shape) - forma nawego data freima
print(type(df.shape))
print(df.shape[1])
'''


'''people = {
    'name':['Bob','Mary', 'John', 'Sara'],
    'surname': ['Smith','Gold', 'Watson', 'Brown'],
    'email': ['bob.smithexample.com', 'Mary.Goldexmaple.com', 'John.Goldexample.com', 'Sara.brownexmaple.com'],
}'''




'''print(df.iloc[1:4])
print(type(df.iloc[1:4]))
print(df.head(1))
new_df = df.iloc[1:3]
print(new_df)'''





#for item in df.iloc[2]:
   # print(item)
#df.head() pokazqvaet pervqe 5 po umol4aniju
#df.tail() pokazqvaet s konca
#print(people['name'][0],people['surname'][0], people['email'][0])
#df = pd.DataFrame(people)
#print(type(df['email'][1:4]))
#df.ilock vqvodit konkretnqe danqe(vqrezaet) s square skobkah vqbiraem index mozno vqvodit konkretnqe srez dopolnitelnqe skobki
#metod iloc rabotaet po indexam
#metod loc rabotaet s strokami