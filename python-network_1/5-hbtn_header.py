#!/usr/bin/python3
"""
Sends a request to the given URL and displays the value of the
X-Request-Id variable in the response header.
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {
        'cfclearance': 'true'
    }
    response = requests.get(url, headers=headers)
    print(response.headers.get('X-Request-Id'))
