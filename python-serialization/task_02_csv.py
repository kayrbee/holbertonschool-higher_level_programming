#!/usr/bin/python3
"""
Use csv and json modules to convert csv to json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a csv file to a json file
    """
    if not csv_filename:
        print(f"[CSV Conversion] CSV file not provided")
        return False

    try:
        with open(csv_filename, "r", encoding="utf-8") as csvf:
            csvreader = csv.DictReader(csvf)  # Create DictReader

            data_list = []  # Store dictionaries in list
            for row in csvreader:  # Read rows into dicts
                data_list.append(row)
            print("Data list: ", data_list)

        with open("data.json", "w", encoding="utf-8") as jf:
            # for item in data_list:
            #     json.dump(data_list, jf)
            json.dump(data_list, jf)
        return True
    except Exception as e:
        print(f"[CSV Conversion] Exception occurred: {e}")
        return False
