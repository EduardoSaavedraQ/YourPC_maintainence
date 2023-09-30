$(document).ready(function() { //Establece la altura de todos los panel-footer en el mismo valor (el más grande).
    var maxHeight = 0;

    $(".panel-footer").each(function(){
        if ($(this).height() > maxHeight) { maxHeight = $(this).height(); }
    });

    $(".panel-footer").height(maxHeight);
});