import os


def generate_invitations(template: str, attendees):
    if not template:
        exit("Template is empty, no output files generated")
    if not attendees:
        exit("No data provided, no output files generated")
    if not isinstance(template, str):
        raise TypeError("Template must be string")
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be list")

    for index, attendee in enumerate(attendees):
        try:
            # Check if output file already exists
            if os.path.exists(f'./output_{index}.txt'):
                continue
            else:
                output = f'output_{index}.txt'

            # Get attendee details
            missing_data_default = "N/A"
            name = attendee['name'] or missing_data_default
            event_title = attendee['event_title'] or missing_data_default
            event_date = attendee['event_date'] or missing_data_default
            event_location = attendee['event_location'] or missing_data_default

            # Insert attendee details into template
            with open(output, 'w', encoding="utf-8") as o:
                invitation = template.replace(
                    "{name}", name).replace("{event_title}", event_title).replace("{event_date}", event_date).replace("{event_location}", event_location)
                o.write(invitation)
        except Exception as e:
            print(f'Error - {e}')
