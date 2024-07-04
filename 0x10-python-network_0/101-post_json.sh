#!/bin/bash
# Script sends a JSON POST and dsiplays the body of responce
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
