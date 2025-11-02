#!/usr/bin/node
const process = require('process');
const args = process.argv;
const a = Number(args[2]);

function factorial (a) {
  if (a === 0 || a === 1 || isNaN(a)) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial(a));
