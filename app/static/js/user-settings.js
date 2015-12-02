$(document).ready(function ($) {
  var nameForm = $("#name");
  nameForm.change(function() {
    $.get("/username-available/" + nameForm.val(), function(data) {

      if (nameForm.parent().hasClass("has-success has-feedback")) {
        nameForm.parent().removeClass("has-success has-feedback");
      }

      if (nameForm.parent().hasClass("has-error has-feedback")) {
        nameForm.parent().removeClass("has-error has-feedback");
      }

      var icon = $("<span></span>");
      icon.addClass("glyphicon form-control-feedback");

      if (data == "1") {
        nameForm.parent().addClass("has-success has-feedback");
        icon.addClass("glyphicon-ok");
      } else {
        nameForm.parent().addClass("has-error has-feedback");
        icon.addClass("glyphicon-remove");
      }

      nameForm.parent().children().filter("span").remove();
      nameForm.parent().append(icon);
    });
  });
});
