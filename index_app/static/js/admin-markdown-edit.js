$('#save-button').on('click', function() {
    $.ajax({
        method: 'POST',
        url: '/save-md/' + $('#filename').text(),
        contentType: 'application/json',
        data: JSON.stringify({
            content: $('#edit-textarea').val()
        }),
        success: function(data) {
            if (data['message'] === 'success') {
                mdui.snackbar('Save success!');
            }
        }
    })
})

if ($('#filename').text() === 'intro.md') {
    $('#back-to-console-link').prop('href', '/admin/metadata');
}