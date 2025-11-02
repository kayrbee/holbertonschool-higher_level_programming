#!/usr/bin/node
const process = require('process');
const args = process.argv;
const size = Number(args[2]);
const c = 'X';
const myErr = 'Missing size';
let line = '';
let i = 0;
let j = 0;

if (args.length === 2 || isNaN(size)) {
  console.log(myErr);
  process.exit(0);
}

for (j = 0; j < size; j++) {
  line += c;
}

while (i < size) {
  console.log(line);
  i++;
}
