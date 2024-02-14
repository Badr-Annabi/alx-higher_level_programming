#!/usr/bin/node

const { dict } = require('./101-data');

const occurencesDict = {};

for (const Id in dict) {
  const occurences = dict[Id];
  if (!occurencesDict[occurences]) {
    occurencesDict[occurences] = [];
  }
  occurencesDict[occurences].push(Id);
}

console.log(occurencesDict);
