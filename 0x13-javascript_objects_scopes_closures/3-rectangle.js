#!/usr/bin/node
/* A class that defines a rectangle and uses the class notation
 this time i create an instance method called print() that will
 print the rectangle using character X */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
