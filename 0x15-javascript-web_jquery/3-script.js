// Script to add the class red to <heder>
// Provided the user clicks on the tag DIV#red_header
// Not using the document.querySelector to select the HTML tag

$('div#red_header').click(function () {
    $('header').addClass('red');
});
