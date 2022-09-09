import csv

with open("some.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["a", "b", "c"])
    writer.writerow(["x", "y", "z"])

with open("some.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(f'{row[0]} {row[1]} {row[2]}')