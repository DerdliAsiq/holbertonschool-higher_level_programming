#!/usr/bin/env python3
<<<<<<< HEAD
=======
"""CSV to JSON module."""
>>>>>>> 7158139 (added new repo)
import csv
import json


def convert_csv_to_json(csv_filename):
<<<<<<< HEAD
    """
    Reads a CSV file and converts it to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion succeeded, False if file not found.
    """
    try:
        # Step 1: Open the CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader uses the headers as keys for the dictionary
            reader = csv.DictReader(csv_file)

            # Convert the reader object into a std Python list of dictionaries
            data_list = list(reader)

        # Step 2: Open/Create the JSON file for writing
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            # Serialize the list of dicts into the file
            # indent=4 makes it readable (pretty-printed) like the example
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        # If the input csv_filename doesn't exist, we return False
        return False
    except Exception as e:
        # It's good practice to catch other unexpected errors too,
        # though the task strictly requires handling file not found.
=======
    """Convert CSV data to JSON format."""
    try:
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
>>>>>>> 7158139 (added new repo)
        return False
