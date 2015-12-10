$(document).ready(function ($) {

    var nameForm = $("#name");
    var nameFormParent = nameForm.parent();

    nameForm.change(function() {
        $.get("/username-available/" + nameForm.val(), function(data) {

            if (nameFormParent.hasClass("has-success has-feedback")) {
                nameFormParent.removeClass("has-success has-feedback");
            }

            if (nameFormParent.hasClass("has-error has-feedback")) {
                nameFormParent.removeClass("has-error has-feedback");
            }

            var icon = $("<span></span>");
            icon.addClass("glyphicon form-control-feedback");

            if (data == "1") {
                nameFormParent.addClass("has-success has-feedback");
                icon.addClass("glyphicon-ok");
            } else {
                nameFormParent.addClass("has-error has-feedback");
                icon.addClass("glyphicon-remove");
            }

            nameFormParent.children().filter("span").remove();
            nameFormParent.append(icon);
        });
    });
});
