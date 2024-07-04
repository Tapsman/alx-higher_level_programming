#!/bin/bash
# Sends request to URL and displays status code responce
curl -s -o /dev/null -w "%{http_code}" "$1"
