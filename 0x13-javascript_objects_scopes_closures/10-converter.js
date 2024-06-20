#!/usr/bin/node
/* This is a function that converts a number from base 10
 to another base that is passed as an argument */

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
