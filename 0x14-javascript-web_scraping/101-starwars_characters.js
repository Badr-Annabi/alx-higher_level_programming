#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';
let allcharacters = [];

request.get(`${url}/${movieId}/`, (error, res, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  allcharacters = data.characters;
  getcharacters(0);
});

const getcharacters = (i) => {
  if (i === allcharacters.length) {
    return;
  }

  request(allcharacters[i], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterdata = JSON.parse(body);
    console.log(characterdata.name);
    getcharacters(i + 1);
  });
};
