#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the value of the X-Request-Id header
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)  # Exit if incorrect number of arguments

    url = sys.argv[1]

    try:
        response = requests.get(url)
        # Raise HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)
