#!/usr/bin/node
/* A script that imports an array from './100-data.js' and then
 and then computes a new array */

const list = require('./100-data').list;
console.log(list);
console.log(list.map((x, i) => x * i));
