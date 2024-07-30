#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (e, cfData) => {
  if (e) {
    console.error(e);
  } else {
    console.log(cfData);
  }
});
