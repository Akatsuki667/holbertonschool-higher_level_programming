#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list")

    if template == "":
        raise ValueError("Template is empty, no output files generated.")
    if attendees == []:
        raise ValueError("No data provided, no output files generated.")

    for idx, attendee in enumerate(attendees, 1):
        new_template = template

        for key, value in attendee.items():
            if value is None:
                value = "N/A"

            new_template = new_template.replace(f"{{{key}}}", str(value))

        with open(f"output_{idx}.txt", "w") as file:
            file.write(new_template)
