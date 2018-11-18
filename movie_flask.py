""" Script used to retrieve data regarding Movies.

Modes:
    `search`: Will search for movies based on a given string
    `ratings`: Will return ratings for movies

Author: Peter Sun
"""
import requests
import api_key
from flask import Flask, render_template, jsonify


app=Flask(__name__)

valid_modes = ['ratings', 'search']

class OMDBException(Exception):
    pass

class OMDBClient():
    movie_url='https://www.omdbapi.com/?apikey={0}&t={1}'
    search_url='https://www.omdbapi.com/?apikey={0}&s={1}'

    def get_movie(self, movie_title):

        print('get_movie url', url)
        response = self.call_api(self.movie_url, movie_title)
        return Movie(response)
    
    def search_movie(self, movie_title):
        response = self.call_api(self.search_url, movie_title)
        movies = response['Search']
        titles = []
        for items in movies:
            titles.append(items['Title'])
        return titles

    def call_api(self, url_format, movie):
        url = url_format.format(api_key.AUTH_KEY, movie)
        response = requests.get(url).json()
        if "Error" in response:
            raise OMDBException('Error occured when calling OMDB API')
        return response


class Movie():
    """
    Movie objects contain all information about a particular movie,
    including the title and rating.
    """

    def __init__(self, movie_data):
        self.title = movie_data['Title']
        self.ratings = movie_data['Ratings']

    def get_title(self):
        """
        get_movie_title is a getter function that returns the movie title.
        """
        return self.title

    def get_rating(self, source = 'Rotten Tomatoes'):
        """
        get_movie_rating is a getter function that returns the rating.
        """
        for rating in self.ratings:
            if rating['Source'] == source:
                return rating['Value']
        return self.ratings


@app.route('/search/<movie_query>', methods=['GET'])
def print_search_results(movie_query):
    """Print list of movies"""
    client = OMDBClient()
    try:
        response = client.search_movie(movie_query)
        # return jsonify({"response": response})
        for index in range(len(response)):
            return jsonify({'{0} : {1}'.format(str(index+1), response[index])})
    except OMDBException as e:
        return jsonify({"error": str(e)})

@app.route('/ratings/<movie_title>', methods=['GET'])
def print_movie_rating(movie_title):
    """Print a movie's title and rating in a formatted string."""
    client = OMDBClient()
    try:
        movie= client.get_movie(movie_title)
        return jsonify({"The rating for {0} is {1}".format( movie.get_title(), movie.get_rating())})
    except OMDBException as e:
        return jsonify({"error": str(e)})

@app.route('/ratings', methods=['POST'])
def print_all_ratings(methods=['POST']):
    """Given a list of movie objects, print the ratings for each one."""
    client=OMDBClient()
    data=request.get_json()
    results={}

    for movie_title in movie_list:
        movie=client.get_movie(movie_title)
        results[movie.get_title()] = movie.get_ratings

    return jsonify({'response': results})


def get_mode_from_user():
    mode=''
    while mode not in valid_modes:
        mode = input('please select {} or {}: \n >'.format(valid_modes[0], valid_modes[1]))
    return mode
   
def user_selection():
    user_selection = input('Please select which movie: \n >')
    return user_selection

# Create one main function that will call everything else.

 
# This line tells Python to run main() when it first opens.
if __name__ == "__main__":
    app.run(debug=True)
    # main()