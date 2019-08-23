$(window).ready(function() {
    $('.mdui-card').addClass('links-to-blank');
    $('.links-to-blank a').attr('target', '_blank');
})

// Admin login logic
$('#admin-login-confirm').on('click', function() {
    let password = $('#admin-password').val();
    $.ajax({
        type: 'POST',
        url: '/login',
        contentType: 'application/json',
        data: JSON.stringify({
            password: password
        }),
        success: function(data) {
            if (data['message'] == 'success') {
                window.location.href = '/admin';
            } else {
                mdui.snackbar('Password wrong.');
            }
        }
    })
})