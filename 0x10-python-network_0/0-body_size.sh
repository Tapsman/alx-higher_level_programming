#!/bin/bash
# This is a bash script that takes a URL, sends a request
curl -s "$1" | wc -c
