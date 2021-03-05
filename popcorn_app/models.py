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
    OTHER = 'Other'


class Rating(FormEnum):
    """Types of Ratings"""
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    ALL = 'All'


class Movie(db.Model):
    """Movie model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.Date)
    genre = db.Column(db.Enum(Genre), default=Genre.OTHER)
    rating = db.Column(db.Enum(Rating), default=Rating.ALL)
    photo_url = db.Column(URLType)


class User(db.Model, UserMixin):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    favorite_movies = db.relationship


favorite_movie_table = db.Table('tags',
                                db.Column('tag_id', db.Integer, db.ForeignKey(
                                    'tag.id'), primary_key=True),
                                db.Column('page_id', db.Integer, db.ForeignKey(
                                    'page.id'), primary_key=True)
                                )
