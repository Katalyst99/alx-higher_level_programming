#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (e, response, body) {
  if (e) {
    console.error(e);
  } else {
    const starwars = JSON.parse(body);
    console.log(starwars.title);
  }
});
