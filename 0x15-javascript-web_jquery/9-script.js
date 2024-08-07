// Script that fetches from url
// URL: https://hellosalut.stefanbohacek.dev/?lang=fr
// And then displays the value of hello from DIV#hello
// while not using the document.querySelector to select the HTML tag

$('doc').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
