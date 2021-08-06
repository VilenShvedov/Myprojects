import requests
from bs4 import BeautifulSoup as BS
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.google.com/search?q=eur+to+byr&oq=eur+to+byr&aqs=chrome..69i57j0i10i22i30j0i22i30l5j0i10i22i30j0i22i30l2.3575j1j4&sourceid=chrome&ie=UTF-8'

r = requests.get(url, timeout=5,headers=headers)

soup = BS(r.content,'html.parser')
#print(soup.find('span', class_="DFlfde SwHCTb").text.replace(',','.'))
print(soup.find('span', class_="DFlfde SwHCTb")['data-value'])
exchange_rate = soup.find('span', class_="DFlfde SwHCTb")['data-value']


def main(rate):
    user_choice = input('Please choose.\n'
                        '1. EUR to BYR\n'
                        '2.BYR to EUR\n'
                        '0. Exit\n'
                        '-->)

    if user_choice == '1':
        pass
    if user_choice == '2':
        pass
    if user_choice == '0':
        print('Good bye')
        exit()
    else:
        print('Choice is out of range')
        main(rate)






#print(soup.find_all('a'))
#print(soup('a', href=re.compile('python')))
#print(soup.find_all('a', href=re.compile('python.org')))
#print(soup.find_all(text='Eesti keeles'))



#match = soup.find_all('h2', align='left')
#print(len(match))
#for h2 in match:
#    print(h2)
#print(soup.div.get_attribute_list('class'))







#print(soup.title)
#print(soup.title.text)
#print(soup.title.name)
#print(soup.head.children)





#with open('picture.png', 'wb') as file:
    #file.write(image.content)

#print(r.ok)
#print(r.headers)
#print(r.status_code)
#print(type(r))
#print(dir(r))
#print(r.text)
#print(r.content)

#r = requests.get('https://xkcd.com/353/', timeout=5, headers=headers)
#image = requests.get('https://imgs.xkcd.com/comics/python.png')