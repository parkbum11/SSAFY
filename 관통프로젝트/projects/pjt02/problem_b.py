import requests
from kobis import URLMaker


def get_movie_cd(title, director):
    url_maker = URLMaker('8b8d7afd9167b675183b991c07132e00')
    my_url = url_maker.get_url('movie', 'searchMovieList')
    para = {
        'movieNm': title,
        'directorNm': director,
    }
    res_b = requests.get(my_url, params=para).json()
    movies = res_b.get('movieListResult').get('movieList')
    
    if movies[0]['movieCd']:
        return movies[0]['movieCd']
    else:
        return 0
        
    return movies


if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색합니다.
    print(get_movie_cd('기생충', '봉준호'))