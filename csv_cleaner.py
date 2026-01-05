import csv

with open("data/input.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)