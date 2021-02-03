function upload_img(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#my_img').attr('src', e.target.result);
            $('.default_profile_image').hide();
            $('.profile_image').show();
        }

        reader.readAsDataURL(input.files[0]);
    }
}
$(function () { //document ready call
    $("#id_image").change(function () {
        upload_img(this);
    });
});