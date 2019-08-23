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
    for articles in publications:
        pub_dom += f'<div class="mdui-typo"><h4 class="mdui-m-t-1 mdui-m-b-0">{articles["topic"]}</h4></div>' + \
            '<ul class="mdui-list">'
        publication_doms = []
        for article in articles["articles"]:
            link_raw = ''
            if '|' in article:
                link_raw = '|'.join(article.split('|')[1:])
                article = article.split('|')[0]
            publication_split = article.split('.')
            author_raw = publication_split[0]
            title_raw = publication_split[1]
            to_raw = ".".join(publication_split[2:])

            author_strings = [f'<strong>{author}</strong>' if en_name in author or cn_name in author
                else author for author in author_raw.split(',')]

            to_string = ''
            if len(to_raw) > 0:
                to_string = f'{to_raw}<br>' 
            
            link_string = ''
            if len(link_raw) > 0:
                link_string_list = []
                for link_item in link_raw.split('|'):
                    link_split_item = link_item.split(',')
                    link_string_list.append(f'<a href="{link_split_item[1]}">{link_split_item[0]}</a>')
                link_string = ' | '.join(link_string_list)

            publication_doms.append('<li class="mdui-list-item publication-item"><p class="mdui-typo">' + \
                f'<strong>{title_raw}</strong><br>' + \
                ', '.join(author_strings) + '<br>' + \
                to_string + link_string + '</p></li>')
        pub_dom += '<li class="mdui-divider"></li>'.join(publication_doms) + '</ul>'
    return pub_dom