import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/maxmin-ohutemp/'
r = requests.get(url, timeout=5, headers=headers)
soup = BS(r.content, 'html.parser')

contents = soup.find('tbody')

results ={}
for row in contents.find_all('tr'):
    row_data = row.find_all('td')
    results[row_data[0].text] = [row_data[1].text ,row_data[2].text, row_data[3].text]


user_input = input('PLease enter city name: ')
print(f'Maximum temperature: {results[user_input][0]}\n'
      f'Minimum temperature: {results[user_input][1]}')