import json
from pprint import pprint

def movie_info(movie):
    result = {}
    result['id'] = movie['id']
    result['title'] = movie['title']
    result['poster_path'] = movie['poster_path']
    result['vote_average'] = movie['vote_average']
    result['overview'] = movie['overview']
    result['genre_ids'] = movie['genre_ids']
    return result

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    pprint(movie_dict)
    pprint(movie_info(movie_dict))