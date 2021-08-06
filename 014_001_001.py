import requests
from bs4 import BeautifulSoup as BS
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.google.com/search?q=eur+to+byr&oq=eur+to+byr&aqs=chrome..69i57j0i10i22i30j0i22i30l5j0i10i22i30j0i22i30l2.3575j1j4&sourceid=chrome&ie=UTF-8'

r = requests.get(url, timeout=5, headers=headers)

soup = BS(r.content, 'html.parser')
exchange_rate =float(soup.find('span', class_="DFlfde SwHCTb")['data-value'])


def main(rate):
    user_choice = input('Please choose.\n'
                        '1. EUR to BYR\n'
                        '2.BYR to EUR\n'
                        '0. Exit\n'
                        '--> ')
    if user_choice == '1':
        eur_to_byr(rate)
    if user_choice == '2':
        byr_to_eur(rate)
    if user_choice == '0':
        print('Good bye')
        exit()
    else:
        print('Choice is out of range')
        main(rate)

def eur_to_byr(rate):
    try:
        ammount = float(input('Please enter amount in EUR: '))
    except:
        print('Amount you entered is not numeric, please try again!')
        eur_to_byr(rate)
    else:
        print(ammount * rate)
        main(rate)

def byr_to_eur(rate):
    try:
        ammount = float(input('Please enter amount in EUR: '))
    except:
        print('Amount you entered is not numeric, please try again!')
        eur_to_byr(rate)
    else:
        print(ammount / rate)
        main(rate)

main(exchange_rate)