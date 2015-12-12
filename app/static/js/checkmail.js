$(document).ready(check_messages);

setInterval("check_messages();", 60000);

function check_messages() {
    $.get("/checkmail", function (data) {
        if (data == "0") {
            $("#newmails").text("");
        } else {
            $("#newmails").text(data);
        }
    });


}