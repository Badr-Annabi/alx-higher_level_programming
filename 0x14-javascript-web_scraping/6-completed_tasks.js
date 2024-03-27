#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const Completedtasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!Completedtasks[todo.userId]) {
        Completedtasks[todo.userId] = 1;
      } else {
        Completedtasks[todo.userId] += 1;
      }
    }
  });
  console.log(Completedtasks);
});
