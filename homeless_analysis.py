import csv
import matplotlib.pyplot as plt

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

    # Filter data for geoid20 "6037121802"
    geoid20 = "6037121802"
    geoid_data = [row for row in csv_data if row["geoid20"] == geoid20]

    years = []
    sheltered_counts = []
    unsheltered_counts = []
    total_counts = []

    for row in geoid_data:
        year = int(row["year"])
        years.append(year)

        totshelt_count = int(row["totshelt_count"])
        totunshelt_count = int(row["totunshelt_count"])
        sheltered_counts.append(totshelt_count)
        unsheltered_counts.append(totunshelt_count)
        total_counts.append(totshelt_count + totunshelt_count)

    # Reverse the lists to display changes from 2017 to 2022
    years.reverse()
    sheltered_counts.reverse()
    unsheltered_counts.reverse()
    total_counts.reverse()

    sheltered_changes = [sheltered_counts[i] - sheltered_counts[i-1] if i > 0 else 0 for i in range(len(sheltered_counts))]
    unsheltered_changes = [unsheltered_counts[i] - unsheltered_counts[i-1] if i > 0 else 0 for i in range(len(unsheltered_counts))]
    total_changes = [total_counts[i] - total_counts[i-1] if i > 0 else 0 for i in range(len(total_counts))]
    plt.figure(figsize=(10, 6))
    plt.plot(years, sheltered_changes, label="Sheltered Change")
    plt.plot(years, unsheltered_changes, label="Unsheltered Change")
    plt.plot(years, total_changes, label="Total Change")
    plt.xlabel("Year")
    plt.ylabel("Change")
    plt.title(f"Changes in Sheltered, Unsheltered, and Total Counts for geoid20 '{geoid20}'")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
