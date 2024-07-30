#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const UrlReq = process.argv[2];
const fPath = process.argv[3];
request(UrlReq, function (e, response, body) {
  if (e) {
    console.log(e);
  } else {
    fs.writeFile(fPath, body, 'utf8', (e) => {
      if (e) {
        console.log(e);
      }
    });
  }
});
