#!/bin/bash
# This script sends a POST request with a JSON file as the body.
curl -s -X POST -H "Content-Type: application/json" --data-binary @"$2" "$1"
