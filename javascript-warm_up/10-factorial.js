#!/usr/bin/node
const process = require('process');
const args = process.argv;
const a = Number(args[2]);
const myErr = 'NaN';
let result = 1;

if (args.length < 3 || isNaN(a)) {
  console.log(myErr);
  process.exit(0);
}

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial(a));
