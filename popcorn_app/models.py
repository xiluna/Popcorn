from popcorn_app import db
from sqlalchemy_utils import URLType
from flask_login import UserMixin
import enum


class FormEnum(enum.Enum):
    """Enum helper class"""
    @classmethod
    def choices(cls):
        return [(choice.name, choice) for choice in cls]

    def __str__(self):
        return str(self.value)


class Genre(FormEnum):
    """Categories of Movie Genres"""
    OTHER = 'Other'
    ACTION_AND_ADVENTURE = 'Action & Adventure'
    ANIME = 'Anime'
    CHILDREN_AND_FAMILY = 'Children & Family'
    CLASSIC = 'Classic'
    DOCUMENTARIES = 'Documentaries'
    DRAMAS = 'Dramas'
    HORROR = 'Horror'
    MUSIC = 'Music'
    ROMANTIC = 'Romantic'
    SCIFI_AND_FANTASY = 'Sci-fi & Fantasy'
    SPORTS = 'Sports'
    THRILLERS = 'Thrillers'


class Rating(FormEnum):
    """Types of Ratings"""
    ALL = 'All'
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'


class Movie(db.Model):
    """Movie model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.Date)
    description = db.Column(db.String(255))
    genre = db.Column(db.Enum(Genre), default=Genre.OTHER)
    rating = db.Column(db.Enum(Rating), default=Rating.ALL)
    photo_url = db.Column(URLType)
    users_who_favorited = db.relationship(
        'User', secondary='user_movie', back_populates='favorite_movies')


class User(db.Model, UserMixin):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    favorite_movies = db.relationship(
        'Movie', secondary='user_movie', back_populates='users_who_favorited')


favorite_books_table = db.Table('user_movie',
                                db.Column('movie_id', db.Integer,
                                          db.ForeignKey('movie.id')),
                                db.Column('user_id', db.Integer,
                                          db.ForeignKey('user.id'))
                                )
