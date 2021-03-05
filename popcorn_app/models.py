from popcorn_app import db
from sqlalchemy_utils import URLType
from popcorn_app.utils import FormEnum
from flask_login import UserMixin


class Genre(FormEnum):
    """Categories of grocery items."""
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
    TV_SHOWS = 'TV Shows'
