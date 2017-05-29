$(document).ready(function () {
    $('.images').click(function () {
        $(this).closest(".post-wrapper").toggleClass("preview");
        $(this).closest(".post-wrapper").toggleClass("full-size");
        $(this).closest(".comment").toggleClass("hidden");
    });
});