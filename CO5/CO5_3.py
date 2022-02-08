import csv
listofcsv = []
with open('file2.csv') as csv_file:
    file_obj = csv.reader(csv_file)

    for rows in file_obj:
       listofcsv.append(rows)

print(listofcsv)
