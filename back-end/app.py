import requests

from config import server, db_name, username, password, themoviedb_api_key
from models import Comment
from models import Movie

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{username}:{password}@{server}/{db_name}"
db = SQLAlchemy(app)

query = "all"
url = f"https://api.themoviedb.org/3/search/movie?api_key={themoviedb_api_key}&query={query}"


def write_movies_to_db():
    movies = get_movies_from_themoviedb()

    for parsed_movie in movies:
        movie = Movie(
            parsed_movie.id,
            parsed_movie.title,
            parsed_movie.year,
            parsed_movie.overview,
            parsed_movie.poster_path,
            parsed_movie.backdrop_path
        )

        if movie.exists():
            movie_from_db = Movie.get_by_id(movie.id)
        else:
            db.session.add(movie)

    db.session.commit()


def get_movies_from_themoviedb():
    result = requests.get(url)
    return result.json()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
