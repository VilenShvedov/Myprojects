import pandas as pd
import time

pd.set_option('display.max_columns', 7000)

def user_menu():
    stack_overflow_survey = pd.read_csv('devel//names.csv')
    user_choice = input('Please choose:\n'
                        '1. Hobby/pro\n'
                        '2.Age\n'
                        '3.Countrie\n'
                        '4.Currency\n'
                        '0.Exit\n'
                        '-->')
    if user_choice == '1' :
        hobbyist_pro(stack_overflow_survey)
    elif user_choice == '2':
        user_age(stack_overflow_survey)
    elif user_choice == '3':
        countries(stack_overflow_survey)
    elif user_choice == '4':
        curency(stack_overflow_survey)
    elif user_choice == '0':
        pass

def hobbyist_pro(df):
    print(df['Hobbyist'].value_counts())
    sorted_values = df[['Hobbyist', 'Respondent']]



def user_age(df):
    print(f"Respondent minimum age is {df['Age'].min()}")
    print(f"Respondent minimum age is {df['Age'].max()}")
    print(f"Respondent minimum age is {df['Age'].mean()}")
    time.sleep(2)
    user_menu()



def countries(df):
    sorted_values = df[['Country','Respondent']]
    print(sorted_values.groupby('Country').count().sort_values('Respondent', ascending=False))
    print(df['Country'].value_counts())
    time.sleep(2)



def curency(df):
    print(df['CurrencyDesc'].value_counts())


user_menu()