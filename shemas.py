from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.String()
    genre_id = fields.Integer()
    genre = fields.Nested(GenreSchema)
    director_id = fields.Integer()
    director = fields.Nested(DirectorSchema)


movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
