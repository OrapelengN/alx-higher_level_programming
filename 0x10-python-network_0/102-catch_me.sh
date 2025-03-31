#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me with the correct header.
curl -s -H "X-HolbertonSchool-User-Id: 98" 0.0.0.0:5000/catch_me
