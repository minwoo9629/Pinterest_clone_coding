$(document).ready(function () {
    $('#comment_input').click(function () {
        $('.add_comment_btn').show();
        $('.cancel_btn').show()
    });
    $('.cancel_btn').click(function () {
        $(".comment-modal").css({
            "top": (($(window).height()-$(".comment-modal").outerHeight())/2+$(window).scrollTop())+"px",
            "left": (($(window).width()-$(".comment-modal").outerWidth())/2+$(window).scrollLeft())+"px"});
        $('.comment-modal').css('display', 'flex');
        $("body").css("overflow","hidden");
        
        
    });
    $('.comment-modal-close').click(function () {
        $('.comment-modal').hide();
        $("body").css("overflow","auto");
    });
    $('.comment-delete-btn').click(function(){
        $('.comment-modal').hide();
        $('.add_comment_btn').hide();
        $('.cancel_btn').hide()
        $('textarea').val('')
        $("body").css("overflow","auto");

    })
})