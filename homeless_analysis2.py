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

    print("Geoid20 | Year | Sheltered Change | Unsheltered Change | Total Change")
    print("-" * 73)

    for row in csv_data:
        geoid20 = row["geoid20"]
        year = int(row["year"])
        totshelt_count = int(row["totshelt_count"])
        totunshelt_count = int(row["totunshelt_count"])

        if prev_row is not None and prev_row["geoid20"] == geoid20:
            sheltered_change = totshelt_count - int(prev_row["totshelt_count"])
            unsheltered_change = totunshelt_count - int(prev_row["totunshelt_count"])
            total_change = sheltered_change + unsheltered_change

            print("{:7} | {:4} | {:15} | {:17} | {:13}".format(geoid20, year, sheltered_change, unsheltered_change, total_change))

        prev_row = row

if __name__ == "__main__":
    main()
