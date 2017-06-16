from ..app import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.String(255))
    overview = db.Column(db.String(255))
    poster_path = db.Column(db.String(255))
    backdrop_path = db.Column(db.String(255))
    rate = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='movie', lazy='dynamic')

    def __init__(self, title, year, overview, poster_path, backdrop_path, rate, comments):
        self.title = title
        self.year = year
        self.overview = overview
        self.poster_path = poster_path
        self.backdrop_path = backdrop_path
        self.rate = rate
        self.comments = comments
