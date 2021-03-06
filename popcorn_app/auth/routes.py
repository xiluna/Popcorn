from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from popcorn_app.models import User
from popcorn_app.auth.forms import SignUpForm, LoginForm
from popcorn_app import bcrypt

from popcorn_app import app, db

auth = Blueprint("auth", __name__)
