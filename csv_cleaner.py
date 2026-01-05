import csv

def load_data(path):
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def clean_data(rows):
    clean_rows = []
    removed = 0
    for row in rows:
        try:
            if row["name"] and row["age"] and row["score"]:
                row["age"] = int(row["age"])
                row["score"] = int(row["score"])
                clean_rows.append(row)
            else:
                removed += 1
        except ValueError:
            removed += 1
    return clean_rows, removed

def save_data(rows, path):
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

def print_summary(rows, removed):
    scores = [row["score"] for row in rows]
    print("\nSummary Report")
    print("----------------")
    print("Valid rows:", len(rows))
    print("Rows removed:", removed)
    print("Average score:", round(sum(scores) / len(scores), 2))
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))

data = load_data("data/input.csv")
clean_rows, removed = clean_data(data)
save_data(clean_rows, "output/cleaned_output.csv")
print_summary(clean_rows, removed)