import os
import logging


def generate_invitations(template: str, attendees):
    if not template:
        logging.error("Template is empty, no output files generated")
        return
    if not attendees:
        logging.error("No data provided, no output files generated")
        return
    if not isinstance(template, str):
        logging.error("Template must be string")
        return
    if not isinstance(attendees, list):
        logging.error("Attendees must be list")
        return

    for index, attendee in enumerate(attendees):
        # Check if output file already exists
        # output = f'output_{index}.txt'
        output = f'output_{index}.txt'
        if os.path.exists(output):
            continue

        # Handle empty values in key
        for key in attendee:
            if not attendee[key]:
                attendee[key] = 'N/A'

        # Handle missing keys
        event_keys = ['name', 'event_title', 'event_date', 'event_location']
        for key in event_keys:
            attendee.setdefault(key, 'N/A')

        # Get attendee details
        name = attendee['name']
        event_title = attendee['event_title']
        event_date = attendee['event_date']
        event_location = attendee['event_location']

        try:
            # Insert attendee details into template
            with open(output, 'w', encoding="utf-8") as o:
                invitation = template.replace(
                    "{name}", name).replace("{event_title}", event_title).replace("{event_date}", event_date).replace("{event_location}", event_location)
                o.write(invitation)
        except Exception as e:
            logging.error(f'Error writing to file {output} - {e}')
