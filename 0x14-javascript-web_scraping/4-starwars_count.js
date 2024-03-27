#!/usr/bin/node

const request = require('request');
const characterId = '18';
const url = process.argv[2];

request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    const count = data.filter(
      film =>
        film.characters.includes(
          `https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(count);
  }
});
