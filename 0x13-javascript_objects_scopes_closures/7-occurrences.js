#!/usr/bin/node
/** This is the a function that returns the number of
 * occurrences in a list */

exports.nbOccurrences = function (list, searchElement) {
  return list.reduce((a, z) => (z === searchElement ? a + 1 : a), 0);
}
