$('#upload-photo-btn').on('click', function() {
    $('#photo-input')[0].click();
});

$('#photo-input').on('change', function() {
    let photoObj = $('#photo-input')[0].files[0];
    let formData = new FormData();
    formData.append("action", "UploadVMKImagePath");
    formData.append("photo", photoObj);

    $.ajax({
        url: "/upload_file",
        type: "POST",
        data: formData,
        dataType: "json",
        cache: false,
        processData:false,
        contentType: false,
        success: function(data) {
            console.log('success');
        }
    })
})