from flask import Blueprint, render_template


home = Blueprint('/', __name__)


@home.route('/')
@home.route('/home')
def home_page():
    return render_template('home/layout.html')