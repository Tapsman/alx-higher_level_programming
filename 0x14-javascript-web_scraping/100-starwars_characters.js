#!/usr/bin/node
// This is a script that will print all the characters of Star Wars movie.

const request = require('request');
const mID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + mID;

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);
  for (const charURL of result.characters) {
    request(charURL, (err, r, body) => {
      if (err) { console.log(err); }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
