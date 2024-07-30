#!/usr/bin/node
// This is a script that will print the content of a file.

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
