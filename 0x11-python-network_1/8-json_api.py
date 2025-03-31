#!/usr/bin/python3
"""
Takes a letter, sends a POST request to search_user, and displays the result.
"""

import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        # Raise HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        try:
            result = response.json()
            if result:
                if isinstance(result, list):
                    for user in result:
                        if isinstance(user, dict) and "id" in user
                        and "name" in user:
                            print(f"[{user['id']}] {user['name']}")
                else:
                    print("Not a valid JSON")

            else:
                print("No result")

        except json.JSONDecodeError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
