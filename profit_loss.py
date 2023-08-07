# Import necessary modules

from pathlib import Path

import csv

 

# Define the function to process the CSV data

def profitloss_function():

    # Initialize empty lists to store the CSV data and cash changes

    csv_data = []

    profit_changes = []

 

    # Create the file paths for input CSV and output summary_report.txt

    file_path = Path.cwd() / "csv_reports" / "Profits_and_Loss.csv"

    filepath = Path.cwd() / "summary_report.txt"

 

    # Open the CSV file in read mode and create a CSV reader object

    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:

        csv_reader = csv.reader(file)

        next(csv_reader)  # Skip the header row

 

        # Iterate through each row in the CSV file and store them in the csv_data list

        for row in csv_reader:

            csv_data.append(row)

 

    # Calculate the cash changes for each day

    for day in range(1, len(csv_data)):

        change = float(csv_data[day][4]) - float(csv_data[day - 1][4])

        profit_changes.append(change)

 

    # Check if there is a surplus in cash every day

    is_surplus_everyday = True

    for change in profit_changes:

        if change <= 0:

            is_surplus_everyday = False

            break

 

    if is_surplus_everyday:

        highest_profit_surplus = profit_changes[0]

        highest_day = csv_data[1][0]

 

        for day, change in enumerate(profit_changes, start=1):

            if change > highest_profit_surplus:

                highest_profit_surplus = change

                highest_day = csv_data[day][0]

 

        # Write the highest cash surplus information to summary_report.txt

        with filepath.open(mode="a", encoding="UTF-8", newline="") as file:

            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

            file.write(f"[HIGHEST NET PROFIT SURPLUS] Day : {highest_day}, AMOUNT : USD{highest_profit_surplus}\n")

 

    # If there is not a surplus every day, report days with cash deficits

    else:

        with filepath.open(mode="a", encoding="UTF-8", newline="") as file:

            for day, change in enumerate(profit_changes):

                if change < 0:

                    file.write(f"[PROFIT DEFICIT] Day : {csv_data[day + 1][0]}, AMOUNT : USD{change}\n")