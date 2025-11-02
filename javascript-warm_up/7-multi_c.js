#!/usr/bin/node
const process = require('process');
const args = process.argv;
const myString = 'C is fun';
const myErr = 'Missing number of occurrences';
let i = 0;

if (args.length === 2) {
  console.log(myErr);
} else {
  const numIterations = Number(args[2]);
  if (Number.isInteger(numIterations)) {
    while (i < numIterations) {
      console.log(myString);
      i++;
    }
  } else {
    console.log(myErr);
  }
}
