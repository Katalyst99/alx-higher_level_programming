#!/usr/bin/node
const myArg = process.argv.slice(2);
const num = parseInt(myArg[0]);

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(num));
