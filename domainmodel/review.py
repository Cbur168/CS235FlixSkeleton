from datetime import datetime

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie

class Review:
    
    def __init__(self, movie, review_text, rating):
        try:
            if not (1 <= int(rating) <= 10):
                raise ValueError
        except ValueError:
            self.__rating = None
        else:
            self.__rating = rating
        
        self.__movie = movie
        self.__review_text = review_text
        self.__timestamp = datetime.now()
    
    def __repr__(self):
        return f"<Review {self.__movie}>"
    
    def __eq__(self, other):
        return self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp

    @property
    def movie(self):
        return self.__movie
    
    @property
    def review_text(self):
        return self.__review_text
    
    @property
    def rating(self):
        return self.__rating
    
    @property
    def timestamp(self):
        return self.__timestamp
