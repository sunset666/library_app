$("#share_button").click(function () {
    if(!$("#share_lib").is(':visible'))
        $("#share_lib").show(600);
    else
        $("#share_lib").hide(600);
});

$("#add_button").click(function () {
    if(!$("#add_book").is(':visible'))
        $("#add_book").show(600);
    else
        $("#add_book").hide(600);
});


$(document).ready( function () {
    $('#booksTable').DataTable();
});
