from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import views
    app.register_blueprint(views.bp)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    return app
