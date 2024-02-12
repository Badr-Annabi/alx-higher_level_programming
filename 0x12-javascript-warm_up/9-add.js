#!/usr/bin/node

function add (a, b) {
  const arg = process.argv.slice(2);
  console.log(`${parseInt(arg[0]) + parseInt(arg[1])}`);
}

add();
