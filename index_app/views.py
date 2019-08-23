import json
import os
import hashlib

from flask import Blueprint, current_app, render_template, session, request, jsonify

from . import utils


bp = Blueprint('views', __name__)
metadata_filedir = os.path.join('/', 'workdir', 'index_app', 'static', 'data', 'data.json')
data = json.load(open(metadata_filedir, 'r'))


@bp.route('/')
@bp.route('/index')
def index():
    contents = []
    for content in data['contents']:
        try:
            contents.append([content['id'], content['title'], utils.build_markdown(content['file_name'])])
        except FileNotFoundError:
            continue
    
    if 'user' not in session:
        session['user'] = ""

    return render_template('index.html', data=data, 
        intro=utils.build_markdown('intro.md'),  
        publications=utils.build_publications(data['publications'], data['en_name'], data['cn_name']),
        contents=contents, about=utils.build_markdown('/workdir/readme.md', True), admin=(session['user'] == 'admin'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    global data

    if request.method == 'POST':
        if hashlib.sha256(request.json['password'].encode()).hexdigest() == data['password-sha256']:
            session['user'] = 'admin'
            if 'newPassword' in request.get_json():
                update_metadata({'password-sha256': hashlib.sha256(request.json['newPassword'].encode()).hexdigest()})
                return jsonify({'message': 'password-change-success'})
            return jsonify({'message': 'success'})
        else:
            return jsonify({'message': 'password_wrong'})


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session['user'] = ''
        return jsonify({'message': 'success'})


@bp.route('/admin')
def admin_noparam():
    return admin('metadata')


admin_title_dict = {'metadata': 'Meta Data', 'content': 'Content', 'password': 'Password'}

@bp.route('/admin/<topic>')
def admin(topic):
    if session['user'] == 'admin' and topic is not None:
        return render_template(f'admin-{topic}.html', subtitle=admin_title_dict[topic],
            metadata=data)
    else:
        return index()


def update_metadata(new_data_dict):
    global data

    for key, value in new_data_dict.items():
        data[key] = value
    with open(metadata_filedir, 'w') as file:
        file.write(json.dumps(data, indent=2))


@bp.route('/metadata-modify', methods=['GET', 'POST'])
def metadata_modify():
    if request.method == 'POST':
        update_metadata(request.get_json())
        return jsonify({'message': 'success'})