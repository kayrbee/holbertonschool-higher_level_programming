#!/usr/bin/node
const process = require('process');
const args = process.argv;
const numIterations = Number(args[2]);
const myString = 'C is fun';
const myErr = 'Missing number of occurrences';
let i = 0;

if (args.length === 2 || isNaN(numIterations)) {
  console.log(myErr);
} else {
  const numIterations = Number(args[2]);
  while (i < numIterations) {
    console.log(myString);
    i++;
  }
}
