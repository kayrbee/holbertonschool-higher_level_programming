#!/usr/bin/python3
"""
Use csv to convert to/from csv
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    fields = []
    rows = []

    with open(csv_filename, "r", encoding="utf-8") as csvf:
        csvreader = csv.reader(csvf) # Reader object

        fields = next(csvreader) # Read header
        for row in csvreader: # Read rows            
            rows.append(row)
        print("Fields: ", fields)
        print("Rows: ", rows)
        
    with open("data.json", "w", encoding="utf-8") as jf:
        for row in rows:
            for index in range(len(row)):
                print(f"{fields[index]}: {row[index]}")
