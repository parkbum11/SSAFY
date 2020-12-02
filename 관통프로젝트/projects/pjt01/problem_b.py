import json
from pprint import pprint


def movie_info(movie, genres):
    result = {}
    newlist = []

    for i in genres:
        for j in range(len(movie['genre_ids'])):
            if i['id'] == movie['genre_ids'][j]:
                newlist.append(i['name'])
    result['genre_names'] = newlist

    result['id'] = movie['id']
    result['title'] = movie['title']
    result['poster_path'] = movie['poster_path']
    result['vote_average'] = movie['vote_average']
    result['overview'] = movie['overview']
    return result


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))