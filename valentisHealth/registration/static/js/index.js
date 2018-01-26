// document.getElementById("uploadBtn").onchange = function () {
//     document.getElementById("uploadFile").value = this.files[0].name;
// };

$(document).ready(function($) {
    console.log("clicked")
    $(document).on( 'click', ".clickable-row", function() {
        console.log("clicked")
        window.location = $(this).data("href");
    });
});