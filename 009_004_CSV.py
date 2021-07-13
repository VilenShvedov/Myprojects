import csv

with open('string.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('string2.csv', 'w', encoding='utf8') as csv_write:
        csv_writer = csv.writer(csv_write, delimiter=',', lineterminator = '\n')

        for line in csv_reader:
            csv_writer.writerow(line)


with open('string2.csv', 'r', encoding='utf8') as csv_file2:
    csv_reader = csv.reader(csv_file2, delimiter=',', lineterminator=';')
    for line in csv_reader:
        print(line)
#next позволяет пропустить строку
#lineterminator удаляет пустые строки если мы в = укажем что хотим удалить