#!/usr/bin/node
// This is a script that increments an integer value

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = () => myObject.value++;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr(myObject);
console.log(myObject);
