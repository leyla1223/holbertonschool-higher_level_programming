#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib and displays
the response body type, raw content, and utf8 decoded content.
"""


from urllib.request import urlopen


def main():
    """
    Sends a GET request to the given URL, reads the response,
    and prints the type, raw content, and UTF-8 decoded content
    of the body.
    """
    url = "https://intranet.hbtn.io/status"

    # Open the URL and fetch the response
    with urlopen(url) as response:
        # Read the response body in bytes
        body = response.read()

        # Print information about the response
        print("Body response:")
        print("\t- type: {}".format(type(body)))          # Print type of response
        print("\t- content: {}".format(body))             # Print raw bytes content
        print("\t- utf8 content: {}".format(body.decode('utf-8')))  # Print decoded content


if __name__ == "__main__":
    main()
