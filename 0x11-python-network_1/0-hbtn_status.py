#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib and displays the body response.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            utf8_content = body.decode('utf-8')
            print("Body response:")
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")
            print(f"\t- utf8 content: {utf8_content}")
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")
