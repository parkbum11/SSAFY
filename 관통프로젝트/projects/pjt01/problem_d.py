import json


def max_revenue(movies):
    max = 0
    max_title = ''

    for i in movies:
        id_detail = i['id']

        movie_jon = open(f'data/movies/{id_detail}.json', encoding='UTF8')

        if max < id_detail['revenue']:
            max = id_detail['revenue']
            max_title = id_detail['title']
    
    return max_title

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))