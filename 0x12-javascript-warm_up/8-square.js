#!/usr/bin/node
/* This script is to print a square, If the first argument cannot
 be converted to integer, print "Missing size" */

const size = process.argv[2];

if (size === undefined || isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  let i = 0;
  let j = 0;
  for (i = 0; i < parseInt(size); i++) {
    let row = '';
    for (j = 0; j < parseInt(size); j++) {
      row = row + X;
    }
    console.log(row);
  }
}
