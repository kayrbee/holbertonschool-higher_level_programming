#!/usr/bin/node
const process = require('node:process');
const errorString = 'Not a number';
const arg1 = process.argv[2];
const value = Number(arg1);

if (Number.isInteger(value)) {
  console.log('My number:', value);
} else {
  console.log(errorString);
}
