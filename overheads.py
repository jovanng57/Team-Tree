# Import necessary modules
from pathlib import Path
import csv

# Define the function to process the CSV data
def overhead_function():
    # Initialize an empty list to store the CSV data
    csv_data = []

    # Create the file path for the CSV file (assuming it is located in "csv_reports" directory)
    file_path = Path.cwd() / "csv_reports" / "Overheads.csv"

    # Create the file path for the summary_report.txt file
    filepath = Path.cwd() / "summary_report.txt"
    filepath.touch()

    # Open the CSV file in read mode and create a CSV reader object
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        csv_reader = csv.reader(file)

        # Skip the header row in the CSV file
        next(csv_reader)

        # Iterate through each row in the CSV file and store them in the csv_data list
        for row in csv_reader:
            csv_data.append(row)

    # Find the item with the highest value in the second column
    max_value = float(csv_data[0][1])  # Initialize max_value with the first value in the second column
    max_value_item = None

    # Search for the highest value in the second column
    for row in csv_data:
        current_value = float(row[1])
        if current_value > max_value:
            max_value = current_value
            max_value_item = row[0]

    # If the highest value is found, write the result to summary_report.txt
    if max_value_item is not None:

        # Open the summary_report.txt file in write mode and write the result
        with filepath.open(mode="w", encoding="UTF-8") as file:
            file.write(f"[HIGHEST OVERHEAD] {max_value_item.upper()}: {max_value}%\n")