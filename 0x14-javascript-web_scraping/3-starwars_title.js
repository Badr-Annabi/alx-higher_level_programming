#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];

request.get(`${url}/${id}`, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
