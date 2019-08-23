// Logout logic
$('#logout-button').on('click', function() {
    $.ajax({
        type: 'POST',
        url: '/logout',
        success: function(data) {
            if (data['message'] === 'success') {
                window.location.href = '/index';
            }
        }
    })
})