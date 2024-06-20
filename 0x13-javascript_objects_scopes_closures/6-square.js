#!/usr/bin/node
/* This is a class Square that defines a square and inherits from
 Square of 5-square.js */
const supSquare = require('./5-square');

class Square extends supSquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }

    let i = 0;
    for (i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
