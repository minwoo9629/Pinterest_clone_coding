$(document).ready(function () {
    $('.delete_modal_btn').click(function () {
        $(".delete_modal").css({
            "top": (($(window).height() - $(".delete_modal").outerHeight()) / 2 + $(window).scrollTop()) + "px",
            "left": (($(window).width() - $(".delete_modal").outerWidth()) / 2 + $(window).scrollLeft()) + "px"
        });
        $('.delete_modal').css('display', 'flex');
        $("body").css("overflow", "hidden");


    });
    $('.delete_modal_close').click(function () {
        $('.delete_modal').hide();
        $("body").css("overflow", "auto");
    });
});