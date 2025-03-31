#!/usr/bin/python3
"""
Takes GitHub credentials and uses the GitHub API to display the user ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        response.raise_for_status()  # Raise HTTPError for bad responses
        user_data = response.json()
        print(user_data.get("id"))

    except requests.exceptions.RequestException as e:
        print(None)
    except ValueError:
        print(None)
