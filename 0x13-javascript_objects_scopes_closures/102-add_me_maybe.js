#!/usr/bin/node
/* A function that will increment and then calls a function */

exports.addMeMaybe = function (num, theFunction) {
  theFunction(++num);
};
