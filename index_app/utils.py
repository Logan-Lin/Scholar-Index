from markdown import markdown


def build_markdown(filename, full_dir=False):
    if full_dir:
        path = filename
    else:
        path = f'/workdir/index_app/static/markdown/{filename}'
    with open(path, 'r', encoding='utf-8') as file:
        markdown_dom = markdown(file.read(), extensions=['markdown.extensions.tables',
            'markdown.extensions.attr_list',
            'markdown.extensions.def_list',
            'markdown.extensions.fenced_code',
            'markdown.extensions.sane_lists'])
        return markdown_dom


def build_publications(publications, admin_name):
    pub_dom = ''
    for publication_topic, publication_list in publications.items():
        pub_dom += f'<div class="mdui-typo"><h4 class="mdui-m-t-1 mdui-m-b-0">{publication_topic}</h4></div>' + \
            '<ul class="mdui-list">'
        publication_doms = []
        for publication in publication_list:
            author_strings = [f'<strong>{author}</strong>' if author==admin_name else author for author in publication['authors']]

            to_string = ''
            if 'to' in publication:
                to_string = f'{publication["to"]}<br>' 

            link_string = ''
            if 'links' in publication:
                link_string = ' '.join([f'<a href="{link[1]}" target="_blank">{link[0]}</a>' for link in publication['links']]) + '<br>'

            note_string = ''
            if 'note' in publication:
                note_string = f'<strong>Note: </strong>{publication["note"]}<br>'

            publication_doms.append('<li class="mdui-list-item publication-item"><p class="mdui-typo">' + \
                f'<strong>{publication["title"]}</strong><br>' + \
                ', '.join(author_strings) + '<br>' + \
                to_string +  link_string +  note_string + '</p></li>')
        pub_dom += '<li class="mdui-divider"></li>'.join(publication_doms) + '</ul>'
    return pub_dom