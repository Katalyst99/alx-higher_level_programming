#!/usr/bin/node
exports.esrever = function (list) {
  const esreverList = [];
  let i = list.length - 1;
  while (i >= 0) {
    esreverList.push(list[i]);
    i--;
  }
  return esreverList;
};
