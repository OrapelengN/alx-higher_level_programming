#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the value of the X-Request-Id
header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)  # Exit if incorrect number of arguments

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)  # exit on error.
