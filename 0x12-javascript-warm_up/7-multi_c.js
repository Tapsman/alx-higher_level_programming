#!/usr/bin/node
/* This script prints x times "C is fun", if the first argumnet
 cant be coverted to an int, prints "Missing number of occurences" */

const x = process.argv[2];

if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  for (i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}
