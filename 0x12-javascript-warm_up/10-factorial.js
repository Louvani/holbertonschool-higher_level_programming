#!/usr/bin/node

function factorial (a) {
  if (a === 0) {
    return -1;
  }
  if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
const num1 = Number.parseInt(process.argv[2]);
if (isNaN(num1)) {
  console.log(1);
} else {
  const result = factorial(num1, num1 - 1);
  console.log(result);
}
