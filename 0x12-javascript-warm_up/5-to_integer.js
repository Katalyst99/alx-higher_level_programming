#!/usr/bin/node
const myArg = process.argv.slice(2);
const num = parseInt(myArg[0], 10);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
