#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  for (const character of data.characters) {
    request(character, function (err, res, body) {
      if (err) {
        console.error(err);
      }
      const actor = JSON.parse(body).name;
      console.log(actor);
    });
  }
});
