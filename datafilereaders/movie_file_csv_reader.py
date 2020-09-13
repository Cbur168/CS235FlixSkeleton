import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__movies = []
        self.__actors = set()
        self.__directors = set()
        self.__genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                for actor in row['Actors'].split(","):
                    actor = Actor(actor.strip())
                    if actor not in self.__actors:
                        self.__actors.add(actor)
                    movie.add_actor(actor)
                    
                director = Director(row['Director'].strip())
                if director not in self.__directors:
                    self.__directors.add(director)
                movie.director = director

                for genre in row['Genre'].split(','):
                    genre = Genre(genre.strip())
                    if genre not in self.__genres:
                        self.__genres.add(genre)
                    movie.add_genre(genre)

                movie.runtime_minutes = row["Runtime (Minutes)"]
                movie.description = row["Description"]

                self.__movies.append(movie)
                
                index += 1
    
    @property
    def dataset_of_movies(self) -> list:
        return self.__movies
    
    @property
    def dataset_of_actors(self) -> set:
        return self.__actors
        
    @property
    def dataset_of_directors(self) -> set:
        return self.__directors
    
    @property
    def dataset_of_genres(self) -> set:
        return self.__genres
