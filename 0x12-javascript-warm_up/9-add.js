#!/usr/bin/node
/* This script will print the sum of two intger, which is
 first and second */

const first = process.argv[2];
const second = process.argv[3];

function add (a, b) {
  return a + b;
}

const a = parseInt(first);
const b = parseInt(second);

console.log(add(a, b));
