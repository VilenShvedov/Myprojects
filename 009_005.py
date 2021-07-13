import csv

with open('string.csv', 'r', encoding='utf8') as csv_file:
    dict_reader = csv.DictReader(csv_file)
    fieldnames = []
    for line in dict_reader:
        for key in line.keys():
            fieldnames.append(key)


    with open('string.csv','w', encoding='utf8') as csv_w:
        fieldnames = ['Name','Date of birth','Town']
        dict_writer = csv.DictWriter(csv_w,delimiter=',', fieldnames=['Imja', 'Data rozdenija', 'gorod'])
        dict_writer.writeheader()
        for line in dict_reader:
            dict_writer.writerow(line)