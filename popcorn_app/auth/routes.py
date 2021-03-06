from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from popcorn_app.models import User
from popcorn_app.auth.forms import SignUpForm, LoginForm
from popcorn_app import bcrypt

from popcorn_app import app, db

auth = Blueprint("auth", __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Account Created.')
        return redirect(url_for('auth.login'))
    print(form.errors)
    return render_template('signup.html', form=form)
