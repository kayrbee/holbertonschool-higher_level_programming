#!/usr/bin/python3
import os

attendees = [
    {"name": "Alice", "event_title": "Python Conference",
        "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
        "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit",
        "event_date": None, "event_location": "Boston"}
]


def generate_invitations(template: str, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be string")
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be list")
    if not template:
        raise ValueError("Template can't be empty")
    if not attendees:
        raise ValueError("Attendees list can't be empty")

    for index, attendee in enumerate(attendees):
        # Check filepath exists
        if os.path.exists(f'./{template}'):

            # Read from template file
            with open(template, 'r', encoding="utf-8") as t:
                template = t.read()

                # Write to filename output_i.txt
                output = f'output_{index}.txt'

                # Insert attendee name into placeholder
                with open(output, 'w', encoding="utf-8") as o:
                    name = attendee['name']
                    print(name)
                    formatted_name = template.replace(
                        "{name}", name)
                    print(formatted_name)
                    o.write(formatted_name)
                # Find {name} placeholder & replace with attendee name


generate_invitations('template.txt', attendees)
