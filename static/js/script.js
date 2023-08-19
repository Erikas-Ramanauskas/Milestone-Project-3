// materialise enablers
$(document).ready(function () {
    // mobile side nav activation
    $(".sidenav").sidenav();
    //Navigation Dropdown activation
    $(".dropdown-trigger").dropdown();
    // form check
    $("input#input_text, textarea#textarea2").characterCounter();
    // Tooltip activation
    $('.tooltipped').tooltip();
});
