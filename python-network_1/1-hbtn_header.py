#!/usr/bin/python3
"""
This script takes a URL, sends a request to it,
and displays the value of the X-Request-Id header from the response.
"""


import sys
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    with urlopen(req) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
