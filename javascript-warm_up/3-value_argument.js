#!/usr/bin/node
const process = require('node:process');

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
