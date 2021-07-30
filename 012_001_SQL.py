import re

emails = '''
Samplemall@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Sample@example.co.uk
example@example.org'''

urls = '''
https://www.google.com
https://www.wordpress.org
https://www.nasa.gov
https://www.example.net
www.example.net
example.net
'''

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456,7890,
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
321.555.4343
123*555*1234
800-555-1234
900-555-1234
988-123-4355
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. O`Rilley
abc

ball mall hall wall tall
333-333-33333333333333
'''


#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')



matches = pattern.search(text_to_search)
print(matches)


#pattern = re.compile(r'[A-Za-z0-9-\._+]+@[A-Za-z0-9-]+\.[A-Za-z]+(\.*[A-Za-z]+)')
#pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+')
#pattern = re.compile(r'https?://(www\.)?[A-Za-z0-9-]+\.[A-Za-z]+')
#pattern = re.compile(r'(https://|http://)?(www\.)?(\w+)(\.\w+)')
#matches = pattern.finditer(urls)

#subbed_urls = pattern.sub(r'\1\3\4', urls)
#print(subbed_urls)



