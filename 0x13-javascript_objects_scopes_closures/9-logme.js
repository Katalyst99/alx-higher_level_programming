#!/usr/bin/node
let nbArg = 0;
exports.logMe = function (item) {
  console.log(`${nbArg}: ${item}`);
  nbArg++;
};
