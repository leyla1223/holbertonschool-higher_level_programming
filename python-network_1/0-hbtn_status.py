#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status using urllib,
adds the required 'cfclearance' header to bypass firewall,
and prints the response in a specific format.
"""

from urllib.request import Request, urlopen

def main():
    """
    Main function that sends a GET request to the given URL with custom headers
    and displays information about the response body.
    """
    url = "https://intranet.hbtn.io/status"
    headers = {
        "cfclearance": "true"  # Required header to bypass firewall
    }

    req = Request(url, headers=headers)

    with urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    main()
