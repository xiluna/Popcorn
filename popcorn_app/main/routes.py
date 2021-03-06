from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from popcorn_app.models import Movie, User
from popcorn_app.main.forms import MovieForm
from popcorn_app import bcrypt
from popcorn_app import app, db

main = Blueprint("main", __name__)


@main.route('/')
def home():
    all_movies = Movie.query.all()
    all_users = User.query.all()
    return render_template('home.html', all_movies=all_movies, all_users=all_users)
