import json
from pprint import pprint


def movie_info(movies, genres):
    result = []
    movie_detail = {}

    for i in movies:
        newlist = []
        for j in genres:
            for k in range(len(i['genre_ids'])):
                if j['id'] == i['genre_ids'][k]:
                    newlist.append(j['name'])
        
        movie_detail['genre_names'] = newlist
        movie_detail['id'] = i['id']
        movie_detail['title'] = i['title']
        movie_detail['poster_path'] = i['poster_path']
        movie_detail['vote_average'] = i['vote_average']
        movie_detail['overview'] = i['overview']
        result.append(movie_detail)
    
    return result

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))