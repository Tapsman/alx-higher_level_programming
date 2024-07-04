#!/bin/bash
# Takes URl, sends GET to URL, and displays the body responce
curl -sH "X-School-User-Id: 98" "$1"
