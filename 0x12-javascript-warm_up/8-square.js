#!/usr/bin/node
/* This script is to print a square, If the first argument cannot
 be converted to integer, print "Missing size" */

const size = process.argv[2];

if (size === undefined || isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
