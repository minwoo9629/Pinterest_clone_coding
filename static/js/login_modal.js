$(document).ready(function () {
    $('.login_modal_btn').click(function () {
        $(".login-modal").css({
            "top": (($(window).height() - $(".login-modal").outerHeight()) / 2 + $(window).scrollTop()) + "px",
            "left": (($(window).width() - $(".login-modal").outerWidth()) / 2 + $(window).scrollLeft()) + "px"
        });
        $('.login-modal').css('display', 'flex');
        $("body").css("overflow", "hidden");
    });

    $('.login-modal-close').click(function () {
        $('.login-modal').hide();
        $('.error_div').hide()
        $('#username').val('');
        $('#password').val('');
        $("body").css("overflow", "auto");
    });
});