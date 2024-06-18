#!/usr/bin/node
const myArg = process.argv.slice(2);

if (myArg[0]) {
  console.log(myArg[0]);
} else {
  console.log('No argument');
}
