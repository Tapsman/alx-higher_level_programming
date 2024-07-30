#!/usr/bin/node
// The script will print, num of movies where char Wedge Antilles is present

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const result = JSON.parse(body).result;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find((character) => characters.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
