from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# In-memory user store. In a real app this would be a database.
users = {}
users_by_email = {}

class User(UserMixin):
    def __init__(self, id_, email, password):
        self.id = id_
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)


def create_user(email, password):
    user_id = str(len(users) + 1)
    user = User(user_id, email, password)
    users[user_id] = user
    users_by_email[email] = user
    return user


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        user = users_by_email.get(email)
        if user and user.check_password(password):
            login_user(user)
            next_url = request.args.get('next') or '/'
            return redirect(next_url)
        flash('Invalid username or password')
    return render_template('LoginPage.html')


@auth_bp.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@auth_bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('parent_password')
        if email in users_by_email:
            flash('This email is already registered.')
            return render_template('RegisterPage.html')
        user = create_user(email, password)
        login_user(user)
        return redirect('/MyProfile')
    return render_template('RegisterPage.html')


@auth_bp.route('/auth/PracticeLogin', methods=['GET', 'POST'])
def practice_login():
    # Simplified practice login that behaves like normal login
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        user = users_by_email.get(email)
        if user and user.check_password(password):
            login_user(user)
            next_url = request.args.get('next') or '/'
            return redirect(next_url)
        flash('Invalid username or password')
    return render_template('LoginPage.html')
