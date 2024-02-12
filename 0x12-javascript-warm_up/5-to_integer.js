#!/usr/bin/node

const arg = process.argv[2];
const integer = parseInt(arg);

if (!isNaN(integer)) {
  console.log(`My number: ${integer}`);
} else {
  console.log('Not a number');
}
