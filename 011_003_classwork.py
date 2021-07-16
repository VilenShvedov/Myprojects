import pandas as pd
'''
1 Программа определает топ 10 стра по ГДП
2. Выводит строку по названию страны
3. показывает одинаковые значения
'''
def user_menu():
    df = pd.read_csv('2019.csv')
    user_choice = input('Please choose\n'
          '1.Top 10 GDP countries\n'
          '2.Data by country name\n'
          '3.Check if there are equal values in Generosity\n'
          '0.Exit\n'
          '-->')

    if user_choice == '1':
        print_top(df)
    elif user_choice == '2':
        print_by_country_name(df)
    elif user_choice == '3':
        check_doubles(df)
    elif user_choice == '0':
        print('Good bye!')
        exit('Good bye')
    else:
        print(' Choice is out of range')
        user_menu()


def print_top(df):
    try:
        top = abs(int(input('How many values ?')))
        if top > df.shape[0]:
            print(f'There are less entries in df, showing {df.shape[0]}entries ')
            top = df.shape[0]
        elif top == 0:
                print('nothing to show')
                user_menu()
    except:
        print('Not number, try again')
        print_top(df)
    if top != 0:
        print(df.sort_values('GDP per capita', ascending=False).head(top))


def print_by_country_name(df):
    try:
        country = input('Please enter country name')
        if country in df['Country or region'].values:
            print(df.loc[df['Country or region'] == country])
        else:
            raise UserWarning
    except:
        print('Country you entered is not in list')
        choice = input('Would you like to see list of countrie? Y/N')
        if choice == 'Y' or choice == 'y':
            print(df['Country or region'].values)
        print_by_country_name(df)
        user_menu()


def check_doubles(df):
    new_df = df.groupby('Generosity').sum()
    print(df.shape)
    print(new_df.shape)
    if df.shape[0] != new_df.shape[0]:
        print('THere are same values in generosity column')
    else:
        print('There are no same values in generosity column')
user_menu()