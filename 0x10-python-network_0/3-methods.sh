#!/bin/bash
# This script sends an OPTIONS request to a URL and displays the Allow header.
curl -s -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
