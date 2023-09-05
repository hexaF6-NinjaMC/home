import os
from datetime import datetime
from english_dictionary import printRandWord
from flask import render_template, request, flash, redirect, url_for
from helper.Forms import CreateUserForm, LoginForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

# ==============---------------SETUP---------------==============
# # Create the Flask Application
app = Flask(__name__)

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Get a Secret Key
skey = app.config['SECRET_KEY']

# Initialize the database
database = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, database)

# Flask_Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# ==============---------------PAGE RENDERS---------------==============
# Home page
@app.route("/")
def main():
    name = os.environ.get("NAME", "dear viewer")
    random_word = f'Hello, {name}! {printRandWord()}'
    return render_template('blog-home.html', randomWord = random_word)

# Delete database records
@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Users.query.get_or_404(id)

    try:
        database.session.delete(user_to_delete)
        database.session.commit()
        flash("User deleted successfully.", category="success")
        
    except:
        flash("Whoops! There was an error deleting the user, try again.", category="error")

    return redirect(url_for('create_user'))

# Create a User page
@app.route('/user/add', methods=['GET', 'POST'])
def create_user():
    name = None
    form = CreateUserForm()

    # Validate Form
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            # Hash password!
            hashed_pw = generate_password_hash(form.password.data, 'sha256')
            user = Users(
                name=form.name.data,
                email=form.email.data,
                password_hash=hashed_pw
            )
            database.session.add(user)
            database.session.commit()
            flash("User created successfully!", category="success")
        else:
            flash("A user cannot be created with that email address", category="error")
        form.name.data = ''
        form.email.data = ''
        form.password.data = ''
        form.password_confirmation.data = ''

        def __repr__(self):
            return '<Name %r>' % self.name
        
    all_reg_users = Users.query.order_by(Users.date_added)
    return render_template('create-user.html', name=name, form=form, users=all_reg_users)

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    email = None
    password = None
    user_to_check = None
    passed = None
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # Clear the form
        form.email.data = ''
        form.password.data = ''

        # Lookup User by email
        user_to_check = Users.query.filter_by(email=email).first()
        if user_to_check:
            # Check Hash password!
            passed = check_password_hash(user_to_check.password_hash, password)
            if passed:
                login_user(user_to_check)
                flash("Login successful!", category="success")
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect credentials. Try again.", category="error")
        else:
            flash("A user with that email does not exist.", category="error")

    return render_template('login.html', email=email, password=password, form=form, passed=passed)

# Create a Dashboard page
@app.route('/dashboard')
@login_required
def dashboard():
    all_reg_users = Users.query.order_by(Users.date_added)
    return render_template('dashboard.html', users=all_reg_users)

# Create Logout page
@app.route('/logout')
@login_required # You can't log out without logging in!
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for('login'))

# Individual Blog page
@app.route('/blogs/<headingOne>/<template>')
def post_blog(template, headingOne):
    return render_template(f'/blogs/{template}', headingOne=headingOne)

# ==============---------------IN-PAGE RENDERS---------------==============
# Blog render by author
@app.route('/<dir>/<twoInitials>/<filename>')
def render_blog(dir, twoInitials, filename):
    file = request.files[f'/{dir}/{twoInitials}/{filename}']
    with open(file, 'r') as file:
        content = file.read()
        return content

# ==============---------------PAGE ERROR HANDLERS---------------==============
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

class Users(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), nullable=False)
    date_added = database.Column(database.DateTime, default=datetime.utcnow)

    # Do some password hashing!
    password_hash = database.Column(database.String(255), nullable=False)
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# ==============---------------MAIN EXECUTION---------------==============
# The MAIN way to run the Flask app
if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
