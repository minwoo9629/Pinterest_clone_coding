$(document).ready(function () {
    $('.sign_up_modal_btn').click(function () {
        $(".sign_up_modal").css({
            "top": (($(window).height() - $(".sign_up_modal").outerHeight()) / 2 + $(window).scrollTop()) + "px",
            "left": (($(window).width() - $(".sign_up_modal").outerWidth()) / 2 + $(window).scrollLeft()) + "px"
        });
        $('.sign_up_modal').css('display', 'flex');
        $("body").css("overflow", "hidden");
    });

    $('.sign_up_modal_close').click(function () {
        $('.sign_up_form')[0].reset();
        $('.username_error_div').hide()
        $('.password_error_div').hide()
        $('.sign_up_modal').hide();
        $("body").css("overflow", "auto");
    });
});