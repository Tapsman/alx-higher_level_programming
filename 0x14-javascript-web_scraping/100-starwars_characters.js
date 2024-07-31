#!/usr/bin/node
// This is a script that will print all the characters of Star Wars movie.

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/${id}';

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const cont = JSON.parse(body);
    const characters = cont.characters;
    // The script will then print the characters.
    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
	} else {
          const names = JSON.parse(body);
	  console.log(names.name);
	}
      });
    }
  }
});
