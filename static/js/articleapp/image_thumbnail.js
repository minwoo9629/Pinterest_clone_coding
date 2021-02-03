function upload_img(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#my_img').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
    $('.change_box').toggle()
}
$(function () { //document ready call
    $("#id_image").change(function () {
        upload_img(this);
    });
});
$('.delete_image').click(function () {
    $('#input_img').val('');
    $('#my_img').attr('src', '');
    $('.change_box').toggle()
});