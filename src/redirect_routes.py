
from flask import Blueprint, render_template, current_app


from flask import Blueprint, render_template, current_app


redirect_bp = Blueprint('redirect', __name__)

@redirect_bp.route('/')
def redirect_page():
    if current_app.debug:
        return render_template('LoginPage.html')

