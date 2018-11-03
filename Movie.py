""" Script used to retrieve data regarding Movies.

Modes:
    `search`: Will search for movies based on a given string
    `ratings`: Will return ratings for movies

Author: Peter Sun 
"""

import requests
import api_key

url= 'https://www.omdbapi.com/?apikey='+api_key.AUTH_KEY

response=requests.get(url)
response_data=response.json()
# print(response_data)
# print(url)

#https://www.omdbapi.com/?apikey=e7e21344&t=clerks


valid_modes = ['ratings', 'search']
mode = valid_modes[0]


class OMDBClient():
    # def __init__(self, movie_title):
    movie_url='https://www.omdbapi.com/?apikey={0}&t={1}'
    search_url='https://www.omdbapi.com/?apikey={0}&s={1}'
    #     self.movie_title=movie_title
    def get_movie(self, movie_title):
        url = self.movie_url.format(api_key.AUTH_KEY, movie_title)
        response = requests.get(url)
        return Movie(response.json())
    
    def search_movie(self, movie_title):
        url = self.search_url.format(api_key.AUTH_KEY, movie_title)
        # print(url)
        response = requests.get(url)

        response=response.json()
       
        response_search=response['Search']
        # print('response_list',response_list)
        # movie = []
        # for titles in response_list:
        #     movie = titles

        # print('search movie', movie)
        print('response search\n\n',response_search)
        return Movie(response_search)





class Movie():
    """
    Movie objects contain all information about a particular movie,
    including the title and rating.
    """

    def __init__(self, movie_data):
        # if type(movie_data)==
        #     self.title=movie_data['title']
        # elif type(movie_data)==
        #     self.title=movie_data
       
            self.title = movie_data
           
            self.rating = movie_data
       


    def get_title(self):
        """
        get_movie_title is a getter function that returns the movie title.
        """
        titles=[], num=0
        try:
            if type(self.title) is list:
                for movie in self.title:

                    titles.append(movie['Title'])
                    
                    
                return titles

            elif type(self.title) is dict:
                self.title = self.title['Title']
                return self.title
            else:
                pass
            

        except KeyError:
            print('Didn\'t find any title')
            pass

    def get_rating(self):
        """
        get_movie_rating is a getter function that returns the rating.
        """
        # try:
        # if type(self.rating) is list:  
        #         rating=movie['Rating'] for movie in self.rating:
        #         self.rating = title
        #     return self.title

        # elif type(self.title) is dict:
        #     self.title=self.title['Title']
        #     return self.title

        for key in self.rating:
            print(key)
            print(self.rating[key])
            # if key['Source'] == 'Rotten Tomatoes'
            # return value



# print(Movie.get_title())


# def build_movie(movie_title, movie_rating):
#     """Take in the movie title and rating, and return the movie object."""

#     return Movie({'title': movie_title, 'rating': movie_rating})

def print_search_results(movie_titles):
    """Print list of movies"""
    # movie_titles=Movie.get_title()

    for title in movie_titles:
        
        print(title)

def print_movie_rating(movie):
    """Print a movie's title and rating in a formatted string."""
    print("The rating for", movie.get_title(), "is",  movie.get_rating())

def print_all_ratings(movie_list):
    """Given a list of movie objects, print the ratings for each one."""
    for movie in movie_list:
        print("The movie", movie.get_title(), "has a rating of", movie.get_rating())



# Create one main function that will call everything else.
def main():

    """
    Main is the entry point into the program, and it calls into the search or
    ratings functions depending on what the user decides to do.
    """
    title = input('Please input the movie you would like to search for: ')
    movie = OMDBClient()

    mode='search'
    # set up default values for testing
    default_movie_list = ['Clerks', 'Dogma', 'Chasing Amy']
    default_movie = Movie({'title': 'clerks', 'rating':10})
    
    if mode == 'search':
        print_search_results(movie.search_movie(title).get_title())

    elif mode == 'ratings':
        print_movie_rating(default_movie)
    else:
        print('Invalid mode!')

# This line tells Python to run main() when it first opens.
if __name__ == "__main__":
    main()