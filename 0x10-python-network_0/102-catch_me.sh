#!/bin/bash
# Script sends a request to 0.0.0.0:5000 "You got me!" body responce
curl -sX PUT -L -d "user_id=98" --header "origion: HolbertonSchool" 0.0.0.0:5000/catch_me
