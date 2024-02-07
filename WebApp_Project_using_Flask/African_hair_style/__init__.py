from flask import Flask, render_template, request, redirect, url_for, Blueprint
from .views.home import home
from .views.hair_style_afro import afro
from .views.hair_style_couettes import couettes
from .views.hair_style_locks import locks
from .views.hair_style_rasta import rasta

def create_app():
    # ______________________________________ APP SET UP ___________________________________________________________
    app = Flask(__name__, instance_relative_config=True)

    # ______________________________________ LOAD THE DEVELOPMENT CONFIGURATION ______________________________________
    app.config.from_object('config.development')

    # ______________________________________ LOAD THE CONFIGURATION FROM THE INSTANCE FOLDER ________________________
    app.config.from_pyfile('config.py')

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    # app.config.from_envvar('APP_CONFIG_FILE')

    # _____________________________________ BLUEPRINTS REGISTERING ______________________________________________________
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(afro, url_prefix='/afro')
    app.register_blueprint(couettes, url_prefix='/couettes')
    app.register_blueprint(locks, url_prefix='/locks')
    app.register_blueprint(rasta, url_prefix='/rasta')



    return app

