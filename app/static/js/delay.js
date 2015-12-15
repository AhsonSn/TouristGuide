$(function () {
    $('#delaydate').datetimepicker({
       locale: 'hu' 
    });
});

function delayTour(id) {
    var date = $("#delaydate0").val();
    $.get("/tourdelay/" + id + "/" + date, function (data) {
        if (data == 0) {
            $('#errormsg').css('display', 'block');
        } else {
            $('#success').css('display', 'block');
            window.setTimeout(go(id), 1000);
        }
    });
}

function go(id) {
    window.location = ("/view-tour/"+id);
}