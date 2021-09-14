#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  const result = {};
  for (const task of data) {
    if (result[task.userId] && task.completed) {
      result[task.userId] += 1;
    } else if (!result[task.userId]) {
      result[task.userId] = 0;
      if (task.completed) {
        result[task.userId] += 1;
      }
    }
  }
  console.log(result);
});
