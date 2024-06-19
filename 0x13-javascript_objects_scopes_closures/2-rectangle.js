#!/usr/bin/node
/* A class that defines a rectangle and uses the class notation */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
    }
  }
}

module.exports = Rectangle;
