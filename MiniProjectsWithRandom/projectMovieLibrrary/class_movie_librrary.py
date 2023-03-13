class MovieLibrary:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def view_movies(self):
        if len(self.movies) == 0:
            print("No movies found in the library")
        else:
            for movie in self.movies:
                print("Title: ", movie.title)
                print("Director: ", movie.director)
                print("Release Year: ", movie.release_year)
                print("Rating: ", movie.rating)
                print("------------------------------")

    def search_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                print("Title: ", movie.title)
                print("Director: ", movie.director)
                print("Release Year: ", movie.release_year)
                print("Rating: ", movie.rating)
                print("------------------------------")
                return
        print("Movie not found")

    def delete_movie(self, title):
        for index, movie in enumerate(self.movies):
            if movie.title == title:
                self.movies.pop(index)
                print("Movie successfully deleted")
                return
        print("Movie not found")

    def update_movie(self, title, director=None, release_year=None, rating=None):
        for movie in self.movies:
            if movie.title == title:
                if director:
                    movie.director = director
                if release_year:
                    movie.release_year = release_year
                if rating:
                    movie.rating = rating
                print("Movie successfully updated")
                return
        print("Movie not found")


movie_library = MovieLibrary()


movie_library.add_movie(Movie("The Shawshank Redemption", "Frank Darabont", 1994, 9.2))
movie_library.add_movie(Movie("The Godfather", "Francis Ford Coppola", 1972, 9.2))
movie_library.add_movie(Movie("The Godfather: Part II", "Francis Ford Coppola", 1974, 9.0))

