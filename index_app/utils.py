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


def build_publications(publications, en_name, cn_name):
    pub_dom = ''
    for publication_topic, publication_list in publications.items():
        pub_dom += f'<div class="mdui-typo"><h4 class="mdui-m-t-1 mdui-m-b-0">{publication_topic}</h4></div>' + \
            '<ul class="mdui-list">'
        publication_doms = []
        for publication in publication_list:
            publication_split = publication['title'].split('.')
            author_raw = publication_split[0]
            title_raw = publication_split[1]
            to_raw = ""
            for split_row in publication_split[2:]:
                to_raw += split_row

            author_strings = [f'<strong>{author}</strong>' if en_name in author or cn_name in author
                else author for author in author_raw.split(',')]

            to_string = ''
            if len(to_raw) > 0:
                to_string = f'{to_raw}<br>' 

            link_string = ''
            if 'links' in publication:
                link_string = ' '.join([f'<a href="{link[1]}">{link[0]}</a>' for link in publication['links']]) + '<br>'

            publication_doms.append('<li class="mdui-list-item publication-item"><p class="mdui-typo">' + \
                f'<strong>{title_raw}</strong><br>' + \
                ', '.join(author_strings) + '<br>' + \
                to_string +  link_string + '</p></li>')
        pub_dom += '<li class="mdui-divider"></li>'.join(publication_doms) + '</ul>'
    return pub_dom