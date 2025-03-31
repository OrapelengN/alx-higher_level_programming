#!/usr/bin/python3
"""
Takes a URL and email, sends a POST request, and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)  # Exit if incorrect number of arguments

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        # Raise HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request: {e}", file=sys.stderr)
        sys.exit(1)
