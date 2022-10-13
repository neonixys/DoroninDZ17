# Импорт необходимого
from flask import request
from flask_restx import Resource

from config import api, app, db
from models import Movie, Genre, Director
from shemas import movie_schema, movies_schema, genres_schema, genre_schema

# Прописываем _ns
movie_ns = api.namespace('movies')
genre_ns = api.namespace('genres')
director_ns = api.namespace('directors')


# Вьюшки для Movie

@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):  # Вывод всех данных
        query = db.session.query(Movie).all()

        if director_id := request.args.get('director_id'):
            query = db.session.query(Movie).filter(Movie.director_id == director_id)

        if genre_id := request.args.get('genre_id'):
            query = db.session.query(Movie).filter(Movie.genre_id == genre_id)

        return movies_schema.dump(query), 200

    def post(self):  # добавление данных
        req_json = request.json
        try:
            new_movie = Movie(**req_json)
            db.session.add(new_movie)
            db.session.commit()
        except Exception as e:
            print(e)
        return "Movie added", 201


@movie_ns.route('/<int:bid>')
class MoviesViews(Resource):
    def get(self, bid: int):  # вывод данных по id
        try:
            movie = db.session.query(Movie).filter(Movie.id == bid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid):  # замена данных
        movie = db.session.query(Movie).get(bid)
        req_json = request.json

        try:
            movie.name = req_json.get("name")
            movie.year = req_json.get("year")
            movie.title = req_json.get("title")
            movie.description = req_json.get("description")
            movie.trailer = req_json.get("trailer")
            movie.rating = req_json.get("rating")
            movie.genre = req_json.get("genre")
            movie.director = req_json.get("director")

            db.session.add(movie)
            db.session.commit()

        except Exception as e:
            print(e)
        return "Movie updated", 201

    def delete(self, bid):  # удаление данных
        movie = db.session.query(Movie).get(bid)
        try:
            db.session.delete(movie)
            db.session.commit()

        except Exception as e:
            print(e)

        return "Movie deleted", 201


@genre_ns.route('/')
class GenreViews(Resource):
    def get(self):
        query = db.session.query(Genre).all()
        return genres_schema.dump(query), 200

    def post(self):  # добавление данных
        req_json = request.json
        try:
            new_genre = Genre(**req_json)
            db.session.add(new_genre)
            db.session.commit()
        except Exception as e:
            print(e)
        return "Genre added", 201


@genre_ns.route('/<int:bid>')
class GenreViews(Resource):
    def get(self, bid: int):  # #вывод данных по id
        try:
            genre = db.session.query(Genre).filter(Genre.id == bid).one()
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid):  # замена данных
        genre = db.session.query(Genre).get(bid)
        req_json = request.json

        try:
            genre.name = req_json.get("name")

            db.session.add(genre)
            db.session.commit()

        except Exception as e:
            print(e)
        return "Genre updated", 201

    def delete(self, bid):  # удаление данных
        genre = db.session.query(Genre).get(bid)
        try:
            db.session.delete(genre)
            db.session.commit()

        except Exception as e:
            print(e)

        return "Genre deleted", 201


@director_ns.route('/')
class GenreViews(Resource):
    def get(self):  # Получение данных
        director = db.session.query(Director).all()
        return genres_schema.dump(director), 200

    def post(self):  # добавление данных
        req_json = request.json
        try:
            new_director = Director(**req_json)
            db.session.add(new_director)
            db.session.commit()
        except Exception as e:
            print(e)
        return "Director added", 201


@director_ns.route('/<int:bid>')
class DirectorViews(Resource):
    def get(self, bid: int):  # вывод данных по id
        try:
            director = db.session.query(Director).filter(Director.id == bid).one()
            return genre_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid):  # замена данных
        director = db.session.query(Director).get(bid)
        req_json = request.json

        try:
            director.name = req_json.get("name")

            db.session.add(director)
            db.session.commit()

        except Exception as e:
            print(e)
        return "Director updated", 201

    def delete(self, bid):  # удаление данных
        director = db.session.query(Director).get(bid)
        try:
            db.session.delete(director)
            db.session.commit()

        except Exception as e:
            print(e)

        return "Director deleted", 201


if __name__ == '__main__':
    app.run(debug=True)
