#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      nb++;
    }
    i++;
  }
  return nb;
};
