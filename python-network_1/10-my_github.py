#!/usr/bin/python3
"""
This script takes GitHub credentials (username and token),
fetches authenticated user info from GitHub API,
and prints the user ID if authenticated successfully.
"""


import sys
import requests


def main():
    """and here we go again"""
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print("None")


if __name__ == "__main__":
    main()
