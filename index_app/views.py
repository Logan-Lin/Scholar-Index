import json
import os

from flask import Blueprint, current_app, render_template

from . import utils


bp = Blueprint('views', __name__)
data = json.load(open('/workdir/index_app/static/data/data.json', 'r'))


@bp.route('/')
def index():
    return render_template('index.html', data=data, open_positions=utils.build_markdown('open_positions.md'),
        intro=utils.build_markdown('intro.md'), news=utils.build_markdown('news.md'), 
        interests=utils.build_markdown('interests.md'), 
        publications=utils.build_publications(data['publications'], data['name']['en_name']),
        award=utils.build_markdown('award.md'))
