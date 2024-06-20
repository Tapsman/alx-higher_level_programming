#!/usr/bin/node
/* This is a function that prints the number of arguments
 that are already printed */

exports.logMe = function (item) {
  if (typeof this.tally === 'undefined') {
    this.tally = 0;
  }
  console.log(this.tally + ': ' + item);
  this.tally++;
};
