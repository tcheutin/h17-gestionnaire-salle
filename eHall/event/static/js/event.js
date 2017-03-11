$(function() {
    var eventId;
    
    // Set the event ID when a modal is triggered
    $('body').on('click', '[data-toggle="modal"]', function() {
        var callerId = $(this).attr('id');
        
        if(typeof callerId !== "undefined") {
            eventId = callerId.substr(callerId.indexOf('#') + 1);
        }
    });
    
    $('#add').on('show.bs.modal', function() {        
        $.ajax({
            'url': '/event/add/',
            'method': 'GET',
            'success': function(response){
                $('#add-body').html(response);
            }
        });
    });
    
    $('#edit').on('show.bs.modal', function() {        
        $.ajax({
            'url': '/event/'.concat(eventId, '/edit/'),
            'method': 'GET',
            'success': function(response){
                $('#edit-body').html(response);
            }
        });
    });
    
    $('#delete').on('show.bs.modal', function() {        
        $.ajax({
            'url': '/event/'.concat(eventId, '/delete/'),
            'method': 'GET',
            'success': function(response){
                $('#delete-body').html(response);
            }
        });
    });
    
    $('#statistics').on('show.bs.modal', function() {        
        $.ajax({
            'url': '/event/'.concat(eventId, '/statistics/'),
            'method': 'GET',
            'success': function(response){
                $('#statistics-view').html(response);
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
            'url': '/event/add/',
            'data': formData,
            'method': 'POST',
            'contentType': false,
            'processData': false,
            'success': function(response){
                $('#event-table').html(response);
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
            'url': '/event/'.concat(eventId, '/edit/'),
            'data': formData,
            'method': 'POST',
            'contentType': false,
            'processData': false,
            'success': function(response){
                $('#event-table').html(response);
            }
        });
    });
    
    $('#delete-button').on('click', function() {
        var form = $('#delete-form')[0];
        var formData = new FormData(form);
        
        $.ajax({
            'url': '/event/'.concat(eventId, '/delete/'),
            'data': formData,
            'method': 'POST',
            'contentType': false,
            'processData': false,
            'success': function(response){
                $('#event-table').html(response);
            }
        });
    });
});