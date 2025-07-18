#!/usr/bin/python3
"""
This module provides a function to generate personalized invitations
from a given template and a list of attendee dictionaries.
"""


import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitations for each attendee.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries with attendee information.

    Returns:
        None
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Loop through each attendee
    for idx, attendee in enumerate(attendees, start=1):
        personalized = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key) if attendee.get(key) is not None else "N/A"
            personalized = personalized.replace(f'{{{key}}}', str(value))

        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
