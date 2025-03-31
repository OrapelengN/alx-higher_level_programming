#!/usr/bin/python3
"""
Lists 10 commits of a GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except (AttributeError, KeyError, ValueError):
        print("Error: Could not process the response.")
