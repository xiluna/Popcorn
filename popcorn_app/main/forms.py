from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from popcorn_app.models import Genre, Rating, Movie


class MovieForm(FlaskForm):
    """Form to create a movie"""
    title = StringField('Movie Title',
                        validators=[DataRequired(), Length(min=1, max=80)])
    publish_date = DateField('Date Published')
