#!/usr/bin/node
/* A script that will print a message depending on the
 number of arguments passed */

const args = process.argv;

if (args.range <= 2) {
  console.log('No argument');
} else if (args.range === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
