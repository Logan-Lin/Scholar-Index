import json
import os

from flask import Blueprint, current_app, render_template

from . import utils


bp = Blueprint('views', __name__)
data = json.load(open('/workdir/index_app/static/data/data.json', 'r'))


@bp.route('/')
def index():
    contents = []
    for content in data['contents']:
        try:
            contents.append([content['id'], content['title'], utils.build_markdown(content['file_name'])])
        except FileNotFoundError:
            continue
    return render_template('index.html', data=data, 
        intro=utils.build_markdown('intro.md'),  
        publications=utils.build_publications(data['publications'], data['name']['en_name']),
        contents=contents)
