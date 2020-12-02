import requests
from kobis import URLMaker
import json


def filmo_count(people, movie):
    url_maker = URLMaker('8b8d7afd9167b675183b991c07132e00')
    my_url = url_maker.get_url('people', 'searchPeopleList')
    para = {
        'peopleNm': people,
        'filmoNames': movie,
    }
    res = requests.get(my_url, params=para).json()
    movies = res.get('peopleListResult').get('peopleList')[0].get('filmoNames')
    movies = movies.split('|')
    return len(movies)




if __name__ == '__main__':
    # 배우 이름과 작품을 이용하여 총 해당 배우가 몇 작품에 출연했는지 출력합니다.
    print(filmo_count('다우니', '아이언맨'))