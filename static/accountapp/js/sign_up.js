$('.sign_up_btn').on('click', function (event) {
    event.preventDefault();
    var formData = $('.sign_up_form').serialize();
    var action = $('.sign_up_form').attr('action');
    var method = $('.sign_up_form').attr('method');
    $.ajax({
        url: action,
        type: method,
        data: formData
    }).done(function () {
        location.reload();
        
    }).fail(function(data){
        console.log(data)
        console.log(data.responseJSON)
        if(data.responseJSON.hasOwnProperty('username')){
            $('#username_error_message').text(data.responseJSON.username);
            $('.username_error_div').show();
        }
        $('#password_error_message').text(data.responseJSON.password2);
        $('.password_error_div').show();
    });
});