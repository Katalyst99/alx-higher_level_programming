#!/usr/bin/node
const myArg = process.argv.slice(2);
const arg1 = parseInt(myArg[0]);
const arg2 = parseInt(myArg[1]);

function add (a, b) {
  const sum = a + b;
  return sum;
}
console.log(add(arg1, arg2));
