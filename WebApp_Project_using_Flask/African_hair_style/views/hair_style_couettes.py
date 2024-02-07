from flask import Blueprint, render_template


couettes = Blueprint('couettes', __name__)



@couettes.route('/')
def couettes_page():
    return render_template('hair_style_couettes/layout.html')