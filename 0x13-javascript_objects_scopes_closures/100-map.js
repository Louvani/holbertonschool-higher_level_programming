#!/usr/bin/node

const firstList = require('./100-data').list;
console.log(firstList);
const map1 = firstList.map((x, index) => x * index);
console.log(map1);
