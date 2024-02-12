#!/usr/bin/node

const arg = process.argv[2];
const integer = parseInt(arg);

if (isNaN(integer)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < arg) {
    const letter = 'X';
    console.log(letter.repeat(arg));
    i++;
  }
}
