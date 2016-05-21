from model.user import User
from model.movie import Movie

def test_add_movie(app):
    app.ensure_login_as(User.Admin())
    app.ensure_bad_movie_not_added(Movie.Bad())
    app.ensure_logout()
