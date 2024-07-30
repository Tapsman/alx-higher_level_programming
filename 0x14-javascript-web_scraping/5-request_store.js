#!/usr/bin/node
// This is a script that will get the content a webpage and stores in a file.

const fs = require('fs');
const request = require('request');
request(process.argv[2].pipe(fs.createWriteStream(process.argv[3]));
