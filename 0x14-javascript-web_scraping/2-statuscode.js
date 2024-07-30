#!/usr/bin/node
const request = require('request');
const urlReq = process.argv[2];

request(urlReq, function (e, response) {
  if (e) {
    console.error(e);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
