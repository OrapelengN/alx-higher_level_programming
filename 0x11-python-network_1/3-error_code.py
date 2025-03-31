#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the response body or error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)  # Exit if incorrect number of arguments

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)
