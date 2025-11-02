#!/usr/bin/node
const process = require('process');
const myArgs = process.argv;
const numArgs = +myArgs.length;

if (numArgs == 2) {
    console.log('No argument');
} else if (numArgs == 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
