import csv

with open("data/input.csv", newline="") as file:
    reader = csv.DictReader(file)

    clean_rows = []

    for row in reader:
        if row["name"] and row["age"] and row["score"]:
            clean_rows.append(row)

    for row in clean_rows:
        row["age"] = int(row["age"])
        row["score"] = int(row["score"])