#!/usr/bin/node
const process = require('process');
const args = process.argv.slice(2).map(Number);

if (args.some(isNaN) || args.length < 2) {
  console.log(0);
  process.exit(0);
}

args.sort((a, b) => a - b);
console.log(args[args.length - 2]);
