from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        try:
            self.__release_year = int(release_year)
            if self.__release_year < 1900:
                raise ValueError
        except ValueError:
            self.__release_year = None

        self.__description = ""
        self.__director = Director("")
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0


    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @property
    def director(self) -> Director:
        return self.__director
    
    @property
    def actors(self) -> list:
        return self.__actors
    
    @property
    def genres(self) -> list:
        return self.__genres
    
    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes
    
    @description.setter
    def description(self, new):
        if type(new) == str:
            self.__description = new.strip()

    @director.setter
    def director(self, director):
        if type(director) == Director:
            self.__director = director
    
    @actors.setter
    def actors(self, actors):
        if type(actors) == list:
            self.__actors = actors
    
    @genres.setter
    def genres(self, genres):
        if type(genres) == list:
            self.__genres = genres
    
    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if int(runtime_minutes) < 0:
            raise ValueError
        else:
            self.__runtime_minutes = int(runtime_minutes)

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return self.__title == other.__title and self.__release_year == other.__release_year
    
    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__release_year < other.__release_year
        return self.__title < other.__title
    
    def __hash__(self):
        return hash((self.__title, self.__release_year))
    
    def add_actor(self, actor):
        if type(actor) == Actor:
            self.__actors.append(actor)
    
    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.pop(self.__actors.index(actor))
    
    def add_genre(self, genre):
        if type(genre) == Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.pop(self.__genres.index(genre))
