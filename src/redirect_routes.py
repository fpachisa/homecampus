from flask import Blueprint, render_template, current_app

redirect_bp = Blueprint('redirect', __name__)

@redirect_bp.route('/')
def redirect_page():
    """Serve the landing page.

    In debug mode the local development server should present the
    main page instead of the production redirect so developers can
    browse the site without being forwarded to ``homecampus.com.sg``.
    """
    if current_app.debug:
        return render_template('MainPage.html')
    return render_template('RedirectPage.html', section='content')

