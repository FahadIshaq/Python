import csv
import re

def add_zip_column_to_csv(file_path):
    with open(file_path, mode ='r') as file:
        csvreader = csv.reader(file)
        headers = next(csvreader)
        rows = [row for row in csvreader]

    # Extract England ZIP codes using regex
    zip_codes = []
    for row in rows:
        address = row[1]
        match = re.search(r'[A-Za-z]{1,2}\d[A-Za-z\d]?\s?\d[A-Za-z]{2}', address)
        zip_code = match.group(0) if match else "N/A"
        zip_codes.append(zip_code)

    # Insert the new "ZIP Code" column header
    headers.insert(1, "ZIP Code")

    # Insert ZIP codes into existing rows
    for i, row in enumerate(rows):
        row.insert(1, zip_codes[i])

    # Write the new CSV file
    with open(file_path, mode='w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(headers)
        for row in rows:
            csvwriter.writerow(row)

# Usage
add_zip_column_to_csv('output.csv')
