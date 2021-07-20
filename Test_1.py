import pandas as pd

user_choice = input('Please choose\n'
                    '1.Hobby or work\n'
                    '2.Age\n'
                    '3.Countries\n'
                    '4.CurrencyDesc\n'
                    '-->')

df = pd.read_csv('devel//names.csv')

if user_choice == '1':
        print(df['Hobbyist'].value_counts())
elif user_choice == '2':
        print(df['Age'].value_counts())
elif user_choice == '3':
        print(df['Country'])
        print(df['Country'].value_counts())
elif user_choice =='4':
    print(df['CurrencyDesc']).value_counts
















