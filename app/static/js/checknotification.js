$(document).ready(check_messages);

setInterval("check_messages();", 60000);

function check_messages() {
    $.get("/checknotification", function (data) {
        if (data == "0") {
            $("#newnotification").text("");
        } else {
            $("#newnotification").text(data);
        }
    });


}