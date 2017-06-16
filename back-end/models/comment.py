from ..app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    comment = db.Column(db.String(255))

    def __init__(self, movie_id, name, email, comment):
        self.movie_id = movie_id
        self.name = name
        self.email = email
        self.comment = comment
