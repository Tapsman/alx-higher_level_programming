#!/usr/bin/node

/* clas that defines a square and inherits from rectangle
 4-rectangle.js */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
