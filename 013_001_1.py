import re


pattern = re.compile(r'[0-9A-Fa-f]{3,6}[^0-9A-Fa-f]')
matches = pattern.finditer(test_string)

for match in matches:
    print(match.group()[:-1])


pattern = re.compile(r'\d+[^+]')

pattern = re.compile(r'\b([0-1][0-9]|2[0-3]):[0-5][0-9][^0-9]')

name_pattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+(-[A-Z][a-z]+)?')
address_pattern = re.compile(r'\d{3} [A-Z0-9][a-z]+ St., [A-Z][A-Za-z-\']+[A-Z]{2} \d+')

for name in name_matches:
    if name.group()[-2:] != 'St' and name.group() != 'Vice City' and name.group() != 'South Park' :
        print(name.group())
        names.append(name.group())
        print(name.group())


for address in address_matches:
