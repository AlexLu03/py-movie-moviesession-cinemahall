from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)

    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies.distinct()


def get_movie_by_id(movie_id):
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(
    movie_title,
    movie_description,
    genres_ids=None,
    actors_ids=None,
):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_movie.genres.add(*genres_ids)

    if actors_ids:
        new_movie.actors.add(*actors_ids)

    return new_movie
