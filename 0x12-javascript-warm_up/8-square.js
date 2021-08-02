#!/usr/bin/node

const num = Number.parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let idx = 0;
  let x = '';
  while (idx < num) {
    x += 'X';
    idx += 1;
  }
  idx = 0;
  while (idx < num) {
    console.log(x);
    idx += 1;
  }
}
