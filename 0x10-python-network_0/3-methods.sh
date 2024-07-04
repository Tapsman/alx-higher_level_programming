#!/bin/bash
# Takes in a URL and displays all the HTTP methods the server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
