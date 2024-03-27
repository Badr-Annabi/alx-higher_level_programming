#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';

request.get(`${url}/${movieId}/`, (error, res, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (error, res, body) => {
      if (error) {
        console.log(error);
      }
      const characterdata = JSON.parse(body);
      console.log(characterdata.name);
    });
  }
});
