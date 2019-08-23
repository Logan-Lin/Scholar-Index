$('#content-add-button').on('click', function() {
    $('#content-list').append(`
        <li class="mdui-list-item content-list-item">
            <div class="mdui-col-xs-5">
                <div class="mdui-textfield">
                    <label class="mdui-textfield-label">Title</label>
                    <input class="mdui-textfield-input content-title-input" type="text" value="" required>
                </div>
            </div>
            <div class="mdui-col-xs-5">
                <div class="mdui-textfield">
                    <label class="mdui-textfield-label">ID</label>
                    <input class="mdui-textfield-input content-id-input" type="text" value="" required>
                </div>
            </div>
            <div class="mdui-col-xs-1">
                <button class="mdui-btn mdui-btn-icon mdui-color-amber content-edit-btn mdui-float-right">
                    <i class="mdui-icon material-icons">edit</i>
                </button>
            </div>
            <div class="mdui-col-xs-1">
                <button class="mdui-btn mdui-btn-icon mdui-color-orange-a200 content-delete-btn mdui-float-right">
                    <i class="mdui-icon material-icons">delete</i>
                </button>
            </div>
        </li>
    `);
    mdui.mutation();
});

$('#content-list').on('click', '.content-delete-btn', function(event) {
    $(event.target).parents('.content-list-item').remove();
});

function fetchAllContents() {
    let contents = [];
    $('#content-list .content-list-item').each(function() {
        let id = $(this).find('.content-id-input').val();
        contents.push({
            title: $(this).find('.content-title-input').val(),
            "file_name": id + '.md',
            id: $(this).find('.content-id-input').val()
        });
    })
    return contents;
}

$('#content-list').on('click', '.content-edit-btn', function(event) {
    saveContent();
    let editId = $(event.target).parents('.content-list-item').find('.content-id-input').val();
    window.location.href = '/edit-md/' + editId;
})

function saveContent() {
    console.log(fetchAllContents());
    $.ajax({
        method: 'POST',
        contentType: 'application/json',
        url: '/metadata-modify',
        data: JSON.stringify({
            contents: fetchAllContents()
        }),
        success: function(data) {
            if (data['message'] == 'success') {
                mdui.snackbar('Metadata saved.');
            } else {
                mdui.snackbar('Error occured when saving data.');
            }
        }
    })
};

$('#save-button').on('click', saveContent);