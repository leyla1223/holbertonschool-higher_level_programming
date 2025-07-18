#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles HTTPError exceptions and prints error codes if they occur.
"""


import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
