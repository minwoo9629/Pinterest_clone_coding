$('.like').click(function (event) {
    event.preventDefault();
    var action = $('.like_form').attr('action');
    var method = $('.like_form').attr('method');
    var formData = $('.like_form').serialize();
    $.ajax({
        url: action,
        type: method,
        data: formData,
        dataType: 'json',
    }).done(function (data) {
        $("#count-" + data.pk).html(data.like_count + "개");
        var users = $("#like-user-" + data.pk).text();
        if (data.message === "True") {
            $(".like").css('color', 'red')
            $(".like").html("favorite")
        } else {
            $(".like").css('color', 'black')
            $(".like").html("favorite_border")
        }
        if (users.indexOf(data.nickname) != -1) {
            $("#like-user-" + data.pk).text(users.replace(data.nickname, ""));
        } else {
            $("#like-user-" + data.pk).text(data.nickname + users);
        }
    }).fail(function () {
        alert("로그인이 필요합니다.")
    })
})