from flask import Blueprint, render_template


afro = Blueprint('afro', __name__)



@afro.route('/')
def afro_page():
    return render_template('hair_style_afro/layout.html')