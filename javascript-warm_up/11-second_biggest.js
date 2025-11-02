#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (isNaN(Number(args[2])) || args.length <= 3) {
  console.log(0);
  process.exit(0);
}

args.sort((a, b) => a - b);
console.log(args[args.length - 2]);
