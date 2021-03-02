from flask import Flask
from popcorn_app.config import Config
import os

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object(Config)


from popcorn_app.main.routes import main as main_routes  # nopep8
app.register_blueprint(main_routes)

from popcorn_app.auth.routes import auth as auth_routes  # nopep8
app.register_blueprint(auth_routes)
