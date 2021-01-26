$('.login_btn').on('click', function (event) {
    event.preventDefault();
    var formData = $('.login_form').serialize();
    var action = $('.login_form').attr('action');
    var method = $('.login_form').attr('method');
    $.ajax({
        url: action,
        type: method,
        data: formData
    }).done(function () {
        location.reload()
    }).fail(function(data){
        $('#error_message').text(data.responseJSON.message)
        $('.error_div').show()
    });
});