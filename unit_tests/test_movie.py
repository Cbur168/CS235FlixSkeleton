from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User


class TestDomainClasses:
            
    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None
    
    def test_csv_reader(self):
        filename = 'C:\Bullshit\CS235FlixSkeleton\datafiles\Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()

        print(movie_file_reader.dataset_of_movies)

        print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
        print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
        print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
        print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
    
    def test_movies(self):
        movie = Movie("Moana", 2016)
        print(movie)

        movie2 = Movie("Moana", 1901)
        print(movie.release_year)

        director = Director("Ron Clements")
        movie.director = director
        print(movie.director)

        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        print(movie.actors)

        movie.runtime_minutes = 107
        print("Movie runtime: {} minutes".format(movie.runtime_minutes))

    def test_user(self):
        movie = Movie("Moana", 2016)
        movie.runtime_minutes = 50
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        user1 = User('Martin', 'pw12345')
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        print(user3.time_spent_watching_movies_minutes)
        user3.watch_movie(movie)
        user3.add_review(review)
        print(user3.time_spent_watching_movies_minutes)
        print(user3.watched_movies)
        print(user3.reviews)
        print(user1 == user2)
        print(user1)
        print(user2)
        print(user3)