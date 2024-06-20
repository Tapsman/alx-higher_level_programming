#!/usr/bin/node
/* This a function that will return the reversed version of a list */

exports.esrever = function (list) {
  let t = 0;
  let len = list.length - 1;
  while ((len - t) > 0) {
    const aux = list[len];
    list[len] = list[t];
    list[t] = aux;
    t++;
    len--;
  }
  return list;
};
