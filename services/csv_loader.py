import csv
csv_file = './uploads/csv/file.csv'
with open(csv_file) as csvfile:
    content = csv.reader(csvfile)
    for row in content:
        print(row)
