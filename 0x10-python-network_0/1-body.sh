#!/bin/bash
# This is a bash script that sends a GET requestto URL
# and it will display the body of the responce
curl -sfL "$1" -X GET