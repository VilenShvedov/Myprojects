import requests
from bs4 import BeautifulSoup as BS
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.gammatest.net/course/python/'
full_page = requests.get(url)

soup = BS(full_page.content, 'html.parser')
match = soup.find_all(string=True)
print(match)

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