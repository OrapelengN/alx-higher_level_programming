#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me with the correct header.
# Trying 99
curl -s -L -X PUT -H "X-HolbertonSchool-User-Id: 98" 0.0.0.0:5000/catch_me

# If 99 fails, try 100
# curl -s -L -X PUT -H "X-HolbertonSchool-User-Id: 100" 0.0.0.0:5000/catch_me
