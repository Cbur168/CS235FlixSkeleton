from datetime import datetime

from domainmodel.review import Review
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.movie import Movie
from domainmodel.director import Director

class User:
    
    def __init__(self, user_name, password):
        if type(user_name) == str:
            self.__username = user_name.strip().lower()
        else:
            self.__username = None
        
        if type(password) == str:
            self.__password = password
        else:
            self.__password = None

        self.__watched_movies = []
        self.__reviews = []
        self.__watch_time = 0

    @property
    def user_name(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews
    
    @property
    def time_spent_watching_movies_minutes(self):
        return self.__watch_time
    
    @user_name.setter
    def user_name(self, user_name):
        if type(user_name) == str:
            self.__username = user_name.strip().lower()
        
    @password.setter
    def password(self, password):
        if type(password) == str:
            self.__password = password
    
    @watched_movies.setter
    def watched_movies(self, watched_movies):
        if type(watched_movies) == list:
            self.__watched_movies = watched_movies
    
    @reviews.setter
    def reviews(self, reviews):
        if type(reviews) == list:
            self.__reviews = reviews

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time):
        try:
            if 0 >= int(time):
                raise ValueError
        except ValueError:
            pass
        else:
            self.__watch_time = time
    
    def __repr__(self):
        return f"<User {self.__username}>"
    
    def __eq__(self,other):
        return self.__username == other.__username
    
    def __lt__(self, other):
        return self.__username < other.__username
    
    def __hash__(self):
        return hash((self.__username, self.__password))
    
    def watch_movie(self, movie):
        if type(movie) != Movie:
            return
        self.__watched_movies.append(movie)
        self.__watch_time += movie.runtime_minutes

    def add_review(self, review):
        if type(review) != Review:
            return
        self.__reviews.append(review)
