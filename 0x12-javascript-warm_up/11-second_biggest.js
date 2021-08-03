#!/usr/bin/node

if (!process.argv[2]) {
  console.log(0);
} else if (!process.argv[3]) {
  console.log(0);
} else {
  const list1 = [];
  let idx = 2;
  while (idx < process.argv.length) {
    list1.push(Number.parseInt(process.argv[idx]));
    idx += 1;
  }
  list1.sort(function (a, b) { return a - b; });
  for (idx = list1.length - 2; idx >= 0; idx--) {
    if (list1[idx] !== list1[list1.length - 1]) {
      console.log(list1[idx]);
      break;
    }
  }
}
