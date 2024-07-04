#!/usr/bin/bash
# This is a bash script that takes a URL, sends a request
# to that URL and then displays the size of the body
curl -s "$1" | wc -c
