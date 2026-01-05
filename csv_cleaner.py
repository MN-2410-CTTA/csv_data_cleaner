import csv

with open("data/input.csv", newline="") as file:
    reader = csv.DictReader(file)

    clean_rows = []

    for row in reader:
        if row["name"] and row["age"] and row["score"]:
            clean_rows.append(row)
