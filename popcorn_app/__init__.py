from .models import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from popcorn_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


bcrypt = Bcrypt(app)


from popcorn_app.main.routes import main as main_routes  # nopep8
app.register_blueprint(main_routes)

from popcorn_app.auth.routes import auth as auth_routes  # nopep8
app.register_blueprint(auth_routes)

with app.app_context():
    db.create_all()
