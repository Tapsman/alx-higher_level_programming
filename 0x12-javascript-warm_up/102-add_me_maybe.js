#!/usr/bin/node
/* This function is going to increment and then calls the function */

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
