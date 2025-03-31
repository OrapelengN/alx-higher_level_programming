#!/bin/bash
# This script takes a URL, sends a request to it, and displays the body size.
curl -s "$1" | wc -c
