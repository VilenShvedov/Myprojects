import json

json_string = '''
{
  "people": [
    {
        "name": "Jack Sumers",
        "phone": "555-555-555",
        "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
        "has_license": false
  },
  {
    "name":"Mary Smith",
    "phone":"777-777-777",
    "emails": null,
    "has_license": true
}
    ]
}'''

structured_data = json.loads(json_string)

print(structured_data['people'])
people = structured_data['people']
for person in people:
    del person['phone']
new_json = json.dumps(structured_data)
print(new_json)
print(type(new_json))
