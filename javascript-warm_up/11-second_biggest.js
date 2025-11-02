#!/usr/bin/node
const process = require('process');
const args = process.argv;
const length = args.length;
let max_value = 0;

// console.log("length:", length);

if (isNaN(Number(args[2])) || length <= 3) {
  console.log(max_value);
  process.exit(0);
}

// Find max
// for (i = 2; i < (length - 1); i++) {
//   max_value = args[i];

//   if (max_value < args[i + 1]) {
//     max_value = args[i + 1];
//   }
// }

// console.log(max_value);

args.sort((a, b => a - b));

console.log(args[length - 1]);
