#!/usr/bin/node
const request = require('request');
const urlReq = process.argv[2];

request(urlReq, function (e, response, body) {
  if (e) {
    console.error(e);
  } else {
    const starwars = JSON.parse(body);
    let count = 0;
    starwars.results.forEach((movie) => {
      movie.characters.forEach((ch) => {
        if (ch.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
