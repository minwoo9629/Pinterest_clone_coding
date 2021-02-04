function upload_img(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#my_img').attr('src', e.target.result);
            $('.project_image').show();
            $('.warning_message').css('color', 'blue');
            $('.warning_message').text('사용할 수 있는 이미지입니다.');
        }

        reader.readAsDataURL(input.files[0]);
    }
}
$(function () { //document ready call
    $("#id_image").change(function () {
        upload_img(this);
    });
});