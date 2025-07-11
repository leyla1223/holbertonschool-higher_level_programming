#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the response body (decoded in utf-8).
"""


import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("utf-8")
    req = request.Request(url, data=data)

    with request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
