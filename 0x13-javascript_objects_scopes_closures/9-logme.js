#!/usr/bin/node
let nb_arg = 0;
exports.logMe = function (item) {
  console.log(`${nb_arg}: ${item}`);
  nb_arg++;
};
