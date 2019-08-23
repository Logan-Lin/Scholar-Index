$('#link-add-btn').on('click', function() {
    $('#link-list').append(`<li class="mdui-list-item">
            <div class="mdui-col-xs-4">
                <div class="mdui-textfield">
                    <label class="mdui-textfield-label">Name</label>
                    <input class="mdui-textfield-input link-name-input" type="text" value="" required>
                </div>
            </div>
            <div class="mdui-col-xs-7">
                <div class="mdui-textfield">
                    <label class="mdui-textfield-label">URL</label>
                    <input class="mdui-textfield-input link-url-input" type="text" value="" required>
                </div>
            </div>
            <div class="mdui-col-xs-1">
                <button class="mdui-btn mdui-btn-icon link-delete-btn mdui-float-right mdui-color-orange-a200">
                    <i class="mdui-icon material-icons">delete</i>
                </button>
            </div>
        </li>`);
    mdui.mutation();
});

$('#link-list').on('click', '.link-delete-btn', function(event) {
    $(event.target).parents('.mdui-list-item').remove();
});

$('#publication-panel').on('change', '.publication-topic-input', function(event) {
    $(event.target).parents('.publication-panel-item').find('.publication-panel-title').text($(event.target).val());
});

$('#publication-panel').on('change', '.publication-date-input', function(event) {
    $(event.target).parents('.publication-panel-item').find('.publication-panel-date').text($(event.target).val());
})

$('#publication-panel').on('click', '.publication-topic-delete-btn', function(event) {
    $(event.target).parents('.publication-panel-item').remove();
    mdui.mutation();
});

$('#publication-panel').on('click', '.publication-delete-btn', function(event) {
    $(event.target).parents('li').remove();
});

$('#publication-panel').on('click', '.publication-add-article-btn', function(event) {
    $(event.target).parents('.publication-panel-item').find('.publication-list').append(`
        <li class="mdui-list-item">
            <div class="mdui-col-xs-11">
                <div class="mdui-textfield">
                    <textarea class="mdui-textfield-input publication-cite-input" type="text" required placeholder="Publication cite"></textarea>
                </div>
            </div>
            <div class="mdui-col-xs-1">
                <button class="mdui-btn mdui-btn-icon publication-delete-btn mdui-float-right mdui-color-orange-a200">
                    <i class="mdui-icon material-icons">delete</i>
                </button>
            </div>
        </li>
    `)
})

$('#publication-add-topic-btn').on('click', function() {
    $('#publication-panel').prepend(`
        <div class="mdui-panel-item publication-panel-item">
            <div class="mdui-panel-item-header">
                <div class="mdui-panel-item-title publication-panel-title">New Topic</div>
                <div class="mdui-panel-item-summary publication-panel-date"></div>
                <i class="mdui-panel-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
            </div>
            <div class="mdui-panel-item-body">
                <div class="mdui-row-sm-2 mdui-row-md-3">
                    <div class="mdui-col">
                        <div class="mdui-textfield">
                            <label class="mdui-textfield-label">Topic name</label>
                            <input class="mdui-textfield-input publication-topic-input" type="text" value="" required>
                        </div>
                    </div>
                    <div class="mdui-col">
                        <div class="mdui-textfield">
                            <label class="mdui-textfield-label">Topic date</label>
                            <input class="mdui-textfield-input publication-date-input" type="date" value="{{publications['date']}}" required>
                        </div>
                    </div>
                    <div class="mdui-col">
                        <span class="mdui-float-right">
                            <button class="mdui-btn mdui-ripple mdui-text-color-red publication-topic-delete-btn">
                                <i class="mdui-icon material-icons">delete</i>
                                Delete topic
                            </button>
                            <button class="mdui-btn mdui-ripple publication-add-article-btn">
                                <i class="mdui-icon material-icons">add</i>
                                Add article
                            </button>
                        </span>
                    </div>
                </div>
                <div class="mdui-divider mdui-m-y-2"></div>
                <ul class="mdui-list publication-list">
                </ul>
            </div>
        </div>
    `);
});

$('#save-button').on('click', function() {
    let links = [];
    $('#link-list .mdui-list-item').each(function() {
        links.push([
            $(this).find('.link-name-input').val(),
            $(this).find('.link-url-input').val()
        ])
    });

    let publications = [];
    $('#publication-panel .publication-panel-item').each(function() {
        let articles = [];
        $(this).find('.publication-cite-input').each(function() {
            articles.push($(this).val());
        });
        publications.push({
            topic: $(this).find('.publication-topic-input').val(),
            date: $(this).find('.publication-date-input').val(),
            articles: articles
        });
    });

    $.ajax({
        method: 'POST',
        contentType: 'application/json',
        url: '/metadata-modify',
        data: JSON.stringify({
            title: $('#title-input').val(),
            en_name: $('#en_name-input').val(),
            cn_name: $('#cn_name-input').val(),
            copyright: $('#copyright-input').val(),
            show_about: $('#show-about-swtich').prop('checked'),
            publications: publications,
            "intro-links": links
        }),
        success: function(data) {
            if (data['message'] == 'success') {
                mdui.snackbar('Metadata saved.');
            } else {
                mdui.snackbar('Error occured when saving data.');
            }
        }
    })
});