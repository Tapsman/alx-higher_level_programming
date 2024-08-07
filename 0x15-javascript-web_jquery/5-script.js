// A script that adds an <li> element
// Provided the user clicks on the DIV#add_item
// The new element will be added to UL.my_list

$('div#add_item'.click(function () {
    let elemt = '<li>Item</li>';
    $('ul.my_list').append(elemt);
});
