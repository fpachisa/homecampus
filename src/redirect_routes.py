from flask import Blueprint, render_template

redirect_bp = Blueprint('redirect', __name__)

@redirect_bp.route('/')
def redirect_page():
    return render_template('RedirectPage.html', section='content')
