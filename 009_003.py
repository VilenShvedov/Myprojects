import json

with open('sample3.json', 'r', encoding='utf8') as json_file:
   data = json.load(json_file)
   print(data)
   print(type(data))

people = data['people']
print(people)
for person in people:
    if person['has_license'] == False:
        del person['has_license']
print(people)


with open('sample3_copy.json', 'w', encoding='utf8') as wfile:
    json.dump(data, wfile, indent=2, sort_keys=True)

data2 = json.dumps(data, indent=2)
print(data2)