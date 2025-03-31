#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests and displays
the body response.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        # Raise HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
