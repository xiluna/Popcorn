from flask import Flask
from popcorn_app.config import Config

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object(Config)


from books_app.main.routes import main as main_routes  # nopep8
app.register_blueprint(main_routes)
