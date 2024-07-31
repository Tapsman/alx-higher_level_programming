#!/usr/bin/node
// This is a script that will get the content a webpage and stores in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileStream = fs.createWriteStream(process.argv[3]);

request
  .get(url)
  .pipe(fileStream);
