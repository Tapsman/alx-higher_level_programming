#!/usr/bin/node
/* This script will print 3 lines like, "1-multi_languages.js"
 but in this case, it prints using array of string and a loop */

const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let i = 0;

for (i = 0; i < array.length; i++) {
  console.log(array[i]);
}
