#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id;

function getName (characters, idx) {
  if (characters.length === idx) {
    return;
  }
  request(characters[idx], function (err, res, body) {
    if (err) {
      console.error(err);
    }
    const actor = JSON.parse(body).name;
    console.log(actor);
    getName(characters, ++idx);
  });
}

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const characters = JSON.parse(body).characters;
  getName(characters, 0);
});
