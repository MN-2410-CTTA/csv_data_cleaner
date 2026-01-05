import csv

clean_rows = []
removed_rows = 0
final_rows = []

with open("data/input.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["name"] and row["age"] and row["score"]:
            clean_rows.append(row)
        else:
            removed_rows += 1

    for row in clean_rows:
        try:
            row["age"] = int(row["age"])
            row["score"] = int(row["score"])
            final_rows.append(row)
        except ValueError:
            removed_rows += 1

with open("output/cleaned_output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=clean_rows[0].keys())
    writer.writeheader()
    writer.writerows(clean_rows)

print("Cleaned data saved to output/cleaned_output.csv")

scores = [row["score"] for row in final_rows]

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print("\nSummary Report")
print("---------------")
print("Rows processed:", len(final_rows))
print("Average score:", round(average_score, 2))
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)