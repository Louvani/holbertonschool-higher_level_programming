#!/usr/bin/node

const { list } = require('./100-data');
console.log(list);
const map1 = list.map(x => x * (x - 1));
console.log(map1);
