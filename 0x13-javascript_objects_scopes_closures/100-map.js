#!/usr/bin/node

const firstList = require('./100-data').list;
console.log(firstList);
const map1 = firstList.map(x => x * (x - 1));
console.log(map1);
