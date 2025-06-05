from flask import Flask
from flask_session import Session
from auth_routes import auth_bp, login_manager
from redirect_routes import redirect_bp
from contact_routes import contact_bp
from static_routes import static_bp
from grade_routes import grade_bp
from learn_routes import learn_bp

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = 'HOMECAMPUS25'
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    login_manager.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(redirect_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(static_bp)
    app.register_blueprint(grade_bp)
    app.register_blueprint(learn_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
