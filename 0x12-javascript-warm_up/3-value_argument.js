#!/usr/bin/node
/* This script will print the first argument that will be
 passed to it */

const args = process.argv;

if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
