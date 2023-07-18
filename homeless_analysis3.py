import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

def main():
    file_path = "All Years Homelessness Calculations.csv"
    csv_data = read_csv_file(file_path)

    csv_data.sort(key=lambda x: (int(x["geoid20"]), int(x["year"])))

    prev_row = None

    sheltered_changes = []
    unsheltered_changes = []
    total_changes = []

    for row in csv_data:
        geoid20 = row["geoid20"]
        year = int(row["year"])
        totshelt_count = int(row["totshelt_count"])
        totunshelt_count = int(row["totunshelt_count"])

        if prev_row is not None and prev_row["geoid20"] == geoid20:
            sheltered_change = totshelt_count - int(prev_row["totshelt_count"])
            unsheltered_change = totunshelt_count - int(prev_row["totunshelt_count"])
            total_change = sheltered_change + unsheltered_change

            sheltered_changes.append((geoid20, sheltered_change))
            unsheltered_changes.append((geoid20, unsheltered_change))
            total_changes.append((geoid20, total_change))

        prev_row = row

    # Sort the lists of tuples based on the second element (the change)
    sheltered_changes.sort(key=lambda x: x[1], reverse=True)
    unsheltered_changes.sort(key=lambda x: x[1], reverse=True)
    total_changes.sort(key=lambda x: x[1], reverse=True)

    print("Top 5 Sheltered Changes:")
    for i, (geoid20, change) in enumerate(sheltered_changes[:5]):
        print(f"{i+1}. Geoid20: {geoid20}, Sheltered Change: {change}")

    print("\nTop 5 Unsheltered Changes:")
    for i, (geoid20, change) in enumerate(unsheltered_changes[:5]):
        print(f"{i+1}. Geoid20: {geoid20}, Unsheltered Change: {change}")

    print("\nTop 5 Total Changes:")
    for i, (geoid20, change) in enumerate(total_changes[:5]):
        print(f"{i+1}. Geoid20: {geoid20}, Total Change: {change}")

if __name__ == "__main__":
    main()
