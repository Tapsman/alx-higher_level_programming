#!/usr/bin/node
/* A script that will search for the second biggest number */

const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  let second = parseInt(args[2]);
  let biggest = parseInt(args[3]);
  let i = 2;
  for (i = 2; i < args.length; i++) {
    const curr = parseInt(args[i]);
    if (curr > biggest) {
      second = biggest;
      biggest = curr;
    } else if (curr > second && curr < biggest) {
      second = curr;
    }
  }
  console.log(second);
}
