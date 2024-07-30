#!/usr/bin/node
// The script will print, num of movies where char Wedge Antilles is present

const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((tally, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? 1 + tally
        : tally;
    }, 0));
  }
});
