#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return 'NaN';
  } else {
    return a + b;
  }
}
const num1 = Number.parseInt(process.argv[2]);
const num2 = Number.parseInt(process.argv[3]);
const result = add(num1, num2);
console.log(result);
