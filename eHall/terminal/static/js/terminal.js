$(function() {
    var terminalId;

    // Set the terminal ID when a modal is triggered
    $('body').on('click', '[data-toggle="modal"]', function() {
        var callerId = $(this).attr('id');

        if(typeof callerId !== "undefined") {
            terminalId = callerId.substr(callerId.indexOf('#') + 1);
        }
    });

	// $('#publish').on('show.bs.modal', function() {
  //       $.ajax({
  //           'url': '/terminal/'.concat(terminalId, '/publish/'),
  //           'method': 'GET',
  //           'success': function(response){
  //               $('#publish-body').html(response);
  //           }
  //       });
  //   });
});
