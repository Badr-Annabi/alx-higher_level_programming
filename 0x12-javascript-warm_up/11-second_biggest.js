#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  console.log(sorted[1]);
}
