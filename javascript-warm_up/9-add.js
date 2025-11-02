#!/usr/bin/node
const process = require('process');
const args = process.argv;
const a = Number(args[2]);
const b = Number(args[3]);
const myErr = 'NaN';

if (args.length < 3 || isNaN(a) || isNaN(b)) {
  console.log(myErr);
  process.exit(0);
}

function add (a, b) {
  return (a + b);
}

console.log(add(a, b));
