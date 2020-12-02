import requests
from kobis import URLMaker
from problem_b import get_movie_cd

# 코드가 이쁘지 않아서 주석 추가 했습니다.
def search_movie_info(movie_cd):
    url_maker = URLMaker('8b8d7afd9167b675183b991c07132e00')
    my_url = url_maker.get_url('movie', 'searchMovieInfo')
    para = {
        'movieCd': movie_cd
    }
    res_c = requests.get(my_url, params=para).json()

    # output을 위한 dict생성
    # 'movieNm', 'openDt' Info 출력 및 dict 추가
    data_dict = {}
    output_list = ['movieNm', 'openDt']
    for i in output_list:
        movies = res_c.get('movieInfoResult').get('movieInfo').get(i)
        data_dict[i] = movies
    
    # 'genreNm' Info 출력 및 dict 추가
    movies = res_c.get('movieInfoResult').get('movieInfo').get('genres')
    data_dict['genres'] = movies[0]['genreNm'].split()
    
    # 'actors' Info 출력 및 dict 추가
    # 명세서에 따라서 movies의 값이 있으면 첫 번째 배우 저장 없으면 'noActor' 리턴
    movies = res_c.get('movieInfoResult').get('movieInfo').get('actors')
    if movies[0].get('peopleNm'):
        data_dict['actors'] = movies[0]['peopleNm']
    else:
        data_dict['actors'] = 'noActor'

    return data_dict

if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색하여 변수 movie_cd에 저장합니다.
    movie_cd = get_movie_cd('기생충', '봉준호')
    # movie_cd를 이용하여 상세정보를 조회하여 출력합니다.
    print(search_movie_info(movie_cd))
