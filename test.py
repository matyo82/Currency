import csv
file = open('arz.csv','r')
reader = csv.reader(file)
for row in reader:
    print(row[2])