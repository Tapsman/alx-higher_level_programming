#!/usr/bin/node
// This is a script that will print all the characters of Star Wars movie.
// Then displays one character name by line, in the same order by the list.

const request = require('request');
const mID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + mID;

request(url, async (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);

  for (const charURL of result.characters) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, r, body) => {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
