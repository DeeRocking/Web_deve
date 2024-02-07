from flask import Blueprint, render_template


locks = Blueprint('locks', __name__)



@locks.route('/')
def locks_page():
    return render_template('hair_style_locks/layout.html')