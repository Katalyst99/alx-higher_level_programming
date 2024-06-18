#!/usr/bin/node
const myArg = process.argv.slice(2);
const num = parseInt(myArg[0], 10);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
