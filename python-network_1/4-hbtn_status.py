#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests package
and displays the response content with proper formatting.
"""


import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {
        'cfclearance': 'true'
    }

    response = requests.get(url, headers=headers)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
