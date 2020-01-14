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
        if content['show']:
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
    if request.method == 'POST' and session['user'] == 'admin':
        update_metadata(request.get_json())
        return jsonify({'message': 'success'})

@bp.route('/edit-md/<filename>')
def edit_md(filename):
    if session['user'] == 'admin':
        filename += '.md'
        file_dir = os.path.join('/', 'workdir', 'index_app', 'static', 'markdown', filename)
        file_content = ""
        if os.path.exists(file_dir):
            with open(file_dir, 'r') as file_pt:
                file_content = file_pt.read()

        return render_template('admin-markdown-edit.html', filename=filename, content=file_content,
            subtitle='Editting')
    else:
        return index()

@bp.route('/save-md/<filename>', methods=['GET', 'POST'])
def save_md(filename):
    if request.method == 'POST' and session['user'] == 'admin':
        file_content = request.json['content']
        file_dir = os.path.join('/', 'workdir', 'index_app', 'static', 'markdown', filename)
        with open(file_dir, 'w') as file_pt:
            file_pt.write(file_content)
        return jsonify({'message': 'success'})

@bp.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and session['user'] == 'admin':
        photo = request.files['photo']
        photo_path = os.path.join('static', 'image', photo.filename)
        photo.save(os.path.join('index_app', photo_path))
        update_metadata({'photo': photo_path})

        return jsonify({'message': 'success'})