$(document).ready(function () {
   $("input").change(function () {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#preview').attr('src', e.target.result);
        }
        reader.readAsDataURL(this.files[0]);
   });
});