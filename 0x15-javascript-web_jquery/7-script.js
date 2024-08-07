// A script that will fetch a character name from a URL
// The URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// While not using document.querySelector to select the HTML tag
// The name has to be displayed in the DIV#character

let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data, stat) {
    $('div#character').text(data.name);
});
