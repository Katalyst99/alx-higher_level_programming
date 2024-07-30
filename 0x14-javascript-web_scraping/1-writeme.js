#!/usr/bin/node

const fs = require('fs');
const f = process.argv[2];
const fData = process.argv[3];

fs.writeFile(f, fData, 'utf8', (e) => {
  if (e) {
    console.error(e);
  }
});
