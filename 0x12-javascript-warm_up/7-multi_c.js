#!/usr/bin/node

const num = Number.parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let idx = 0;
  while (idx < num) {
    console.log('C is fun');
    idx += 1;
  }
}
