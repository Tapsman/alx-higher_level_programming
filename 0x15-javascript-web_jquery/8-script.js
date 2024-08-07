// Script that fetches the lists of titles for all movies using URL
// The URL: https://swapi-api.alx-tools.com/api/films/?format=json
// Where all the movie titles will be list in the HTML tag UL#list_movies
// Not using the document.querySelector to select the HTML tag

let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('ul#list_movies').append('<li>${film.title}</li>');
  }
});
