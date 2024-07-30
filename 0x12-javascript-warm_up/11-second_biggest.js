#!/usr/bin/node
const myArg = process.argv.slice(2).map(Number);

if (myArg.length <= 1) {
  console.log(0);
} else {
  const Max = myArg.sort((a, b) => b - a)[1];
  console.log(Max);
}
