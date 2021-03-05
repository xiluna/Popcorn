from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL
from popcorn_app.models import Genre, Rating, Movie


class MovieForm(FlaskForm):
    """Form to create a movie"""
    title = StringField('Movie Title',
                        validators=[DataRequired(), Length(min=1, max=80)])
    description = TextAreaField('Movie Description')
    release_date = DateField('Date Published')
    genre = SelectField('Genre', choices=Genre.choices())
    rating = SelectField('Rating', choices=Rating.choices())
    photo_url = StringField('Photo', validators=[URL()])
    submit = SubmitField("Create")
