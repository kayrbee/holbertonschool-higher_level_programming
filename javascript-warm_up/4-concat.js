#!/usr/bin/node
const process = require('node:process');
const myArgs = process.argv;
const numArgs = +myArgs.length;
const undef = 'undefined';
const spacerString = 'is';

if (numArgs === 2) {
  console.log(undef, spacerString, undef);
} else if (numArgs === 3) {
  console.log(process.argv[2], spacerString, undef);
} else {
  console.log(process.argv[2], spacerString, process.argv[3]);
}
