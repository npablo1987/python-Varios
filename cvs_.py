import csv


cargarcsv = "C:/csv/datos.csv"
with open(cargarcsv) as f:
    reader = csv.reader(f, delimiter=";")
    print(reader)
    for row in reader:
        print(row[0],row[1],row[2],row[3],row[4])


