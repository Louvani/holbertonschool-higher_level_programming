#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  let count = 0;
  for (const result of data.results) {
    for (const character of result.characters) {
      if (character.slice(-4) === '/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
