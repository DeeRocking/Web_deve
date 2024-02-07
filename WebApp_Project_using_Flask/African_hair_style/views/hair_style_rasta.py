from flask import Blueprint, render_template


rasta = Blueprint('rasta', __name__)



@rasta.route('/')
def rasta_page():
    return render_template('hair_style_rasta/layout.html')