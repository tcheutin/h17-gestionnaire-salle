$(function() {
    var auditoriumId;

    // Set the auditorium ID when a modal is triggered
    $('body').on('click', '[data-toggle="modal"]', function() {
        var callerId = $(this).attr('id');

        if(typeof callerId !== "undefined") {
            auditoriumId = callerId.substr(callerId.indexOf('#') + 1);
        }
    });

    $('#add').on('show.bs.modal', function() {
        $.ajax({
            'url': '/auditorium/add/',
            'method': 'GET',
            'success': function(response){
                $('#add-body').html(response);
            }
        });
    });

    $('#edit').on('show.bs.modal', function() {
        $.ajax({
            'url': '/auditorium/'.concat(auditoriumId, '/edit/'),
            'method': 'GET',
            'success': function(response){
                $('#edit-body').html(response);
            }
        });
    });

    $('#delete').on('show.bs.modal', function() {
        $.ajax({
            'url': '/auditorium/'.concat(auditoriumId, '/delete/'),
            'method': 'GET',
            'success': function(response){
                $('#delete-body').html(response);
            }
        });
    });

    $('#events').on('show.bs.modal', function() {
        $.ajax({
            'url': '/auditorium/'.concat(auditoriumId, '/events/'),
            'method': 'GET',
            'success': function(response){
                $('#event-view').html(response);
            }
        });
    });

    $('#add-button').on('click', function() {
        var form = $('#add-form')[0];
        var formData = new FormData(form);
        //var image = $('#image').files[0];
        //if(typeof image !== 'undefined') {
        //    formData.append('image', image);
        //} // TODO support image upload

        $.ajax({
            'url': '/auditorium/add/',
            'data': formData,
            'method': 'POST',
            'contentType': false,
            'processData': false,
            'success': function(response){
                $('body').html(response);
            }
        });
    });

    $('#edit-button').on('click', function() {
        var form = $('#edit-form')[0];
        var formData = new FormData(form);
        //var image = $('#image').files[0];
        //if(typeof image !== 'undefined') {
        //    formData.append('image', image);
        //} // TODO support image upload

        $.ajax({
            'url': '/auditorium/'.concat(auditoriumId, '/edit/'),
            'data': formData,
            'method': 'POST',
            'contentType': false,
            'processData': false,
            'success': function(response){
                $('body').html(response);
            }
        });
    });

    $('#delete-button').on('click', function() {
        var form = $('#delete-form')[0];
        var formData = new FormData(form);

        $.ajax({
            'url': '/auditorium/'.concat(auditoriumId, '/delete/'),
            'data': formData,
            'method': 'POST',
            'contentType': false,
            'processData': false,
            'success': function(response){
                $('body').html(response);
            }
        });
    });
});
