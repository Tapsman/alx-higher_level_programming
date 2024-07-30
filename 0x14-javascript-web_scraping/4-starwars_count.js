#!/usr/bin/node
// The script will print, num of movies where char Wedge Antilles is present

const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    const res = JSON.parse(body).res;
    console.log(res.reduce((tally, movie) => {
      return movie.characters.find((characters) => character.endsWith('/18/'))
        ? 1 + tally
	: tally;
    }, 0));
  }
});

