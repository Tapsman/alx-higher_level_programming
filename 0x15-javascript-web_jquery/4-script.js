// Script that will toggle the class of the <header> element
// Provided the user clicks on the tag DIV#toggle_header

$('div#toggle_header').click(function () {
    $('header').ToggleClass('red');
});
