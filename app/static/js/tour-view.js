$(document).ready(function ($) {

  $(document).delegate('*[data-toggle="lightbox"]:not([data-gallery="navigateTo"])', 'click', function(event) {
    event.preventDefault();
    return $(this).ekkoLightbox({
      onShown: function() {
        if (window.console) {
          return console.log('Checking our the events huh?');
        }
      }
    });
  });
});
