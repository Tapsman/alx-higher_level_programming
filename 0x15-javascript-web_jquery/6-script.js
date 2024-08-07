// A script to update the text <header> element to a new one!
// Provided the user clicks on DIV#update_header
// Not using the document.querySelector to select the HTML tag

$('div#update_header').click(function () {
    $('header').text('New Header!!!');
});
