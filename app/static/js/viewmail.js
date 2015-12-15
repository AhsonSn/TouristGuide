function setread(messageid) {
    $.get("/readmail/" + messageid , function (data) {
        check_messages();
        $("#sor_" + messageid).css("font-weight", "normal");
    });

}

function setreadNotification(messageid) {
    $.get("/readnotification/" + messageid, function (data) {
        check_messages();
        $("#sor_" + messageid).css("font-weight", "normal");
    });

}