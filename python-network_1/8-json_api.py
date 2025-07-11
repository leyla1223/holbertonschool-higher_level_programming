#!/usr/bin/python3
"""
Takes a letter, sends a POST request to a URL with 'q' as parameter,
and prints user info if JSON response is valid and not empty.
"""


import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        json_resp = response.json()
        if json_resp:
            print(f"[{json_resp.get('id')}] {json_resp.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
