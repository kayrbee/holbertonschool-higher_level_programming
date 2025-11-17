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
        raise TypeError("Template must be string")
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be list")

    for index, attendee in enumerate(attendees):
        # Check if output file already exists
        output = f'output_{index}.txt'
        if os.path.exists(output):
            continue

        for key in attendee:
            if not attendee[key]:
                attendee[key] = f'{key}: N/A'

        # Get attendee details
        name = attendee['name']
        event_title = attendee['event_title']
        event_date = attendee['event_date'] or "event_date: N/A"
        event_location = attendee['event_location']

        try:
            # Insert attendee details into template
            with open(output, 'w', encoding="utf-8") as o:
                invitation = template.replace(
                    "{name}", name).replace("{event_title}", event_title).replace("{event_date}", event_date).replace("{event_location}", event_location)
                o.write(invitation)
        except Exception as e:
            logging.error(f'Error writing to file {output} - {e}')
