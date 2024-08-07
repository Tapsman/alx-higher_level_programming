// Script to update text color FF0000 when the user clicks on the tag
// Without the document.querySelector to select the HTML tag

$('div#red_header').click(function () {
    $('header').css('color', '#FF0000');
});
