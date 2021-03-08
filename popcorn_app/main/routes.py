from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import date, datetime
from popcorn_app.models import Movie, User
from popcorn_app.main.forms import MovieForm
from popcorn_app import db

main = Blueprint("main", __name__)


@main.route('/')
def home():
    all_movies = Movie.query.all()
    all_users = User.query.all()
    return render_template('home.html', all_movies=all_movies, all_users=all_users)


@main.route('/create_movie', methods=['GET', 'POST'])
@login_required
def create_movie():
    form = MovieForm()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            release_date=form.release_date.data,
            description=form.description.data,
            genre=form.genre.data,
            rating=form.rating.data,
            photo_url=form.photo_url.data,
        )
        db.session.add(new_movie)
        db.session.commit()
        flash('New movie was created successfully.')
        return redirect(url_for('main.movie_detail', movie_id=new_movie.id))
    return render_template('create_movie.html', form=form)


@main.route('/movie/<movie_id>', methods=['GET', 'POST'])
def movie_detail(movie_id):
    movie = Movie.query.get(movie_id)
    form = MovieForm(obj=movie)
    if form.validate_on_submit():
        movie.title = form.title.data
        movie.release_date = form.release_date.data
        movie.description = form.description.data
        movie.genre = form.genre.data
        movie.rating = form.rating.data
        movie.photo_url = form.photo_url.data

        db.session.commit()

        flash('Movie was updated successfully.')
        return redirect(url_for('main.movie_detail', movie_id=movie_id))
    return render_template('movie_detail.html', movie=movie, form=form)


@main.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).one()
    return render_template('profile.html', user=user)


@main.route('/favorite/<movie_id>', methods=['POST'])
@login_required
def favorite_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie in current_user.favorite_movies:
        flash('Movie already in favorites.')
    else:
        current_user.favorite_movies.append(movie)
        db.session.add(current_user)
        db.session.commit()
        flash('Movie added to favorites.')
    return redirect(url_for('main.movie_detail', movie_id=movie_id))


@main.route('/unfavorite/<movie_id>', methods=['POST'])
@login_required
def unfavorite_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie not in current_user.favorite_movies:
        flash('Movie not in favorites.')
    else:
        current_user.favorite_movies.remove(movie)
        db.session.add(current_user)
        db.session.commit()
        flash('Movie removed from favorites.')
    return redirect(url_for('main.movie_detail', movie_id=movie_id))
