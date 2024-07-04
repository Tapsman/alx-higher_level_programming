#!/bin/bash
# Takes in URL, sends POST request to passed URL, returns responce
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
