import requests
import json
def find_name(id,genres):
    for genre in genres['genres']:
        if genre['id']!=id: continue
        return genre['name']

def find_director(credits,imgURL):
    for credit in credits['crew']:
        if credit['known_for_department']!='Directing':continue
        print(credit)
        tmp_path=credit['profile_path']
        # print(f'{imgURL}{credit['profile_path']}')
        return {'name':credit['name'],'profile_path':f'{imgURL}{tmp_path}'}
genreURL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=85a6946564b671a073402f6de8740a69&language=ko-KR'
movieURL = 'https://api.themoviedb.org/3/movie/popular?api_key=85a6946564b671a073402f6de8740a69&language=ko-KR'
creditsURL1 = 'https://api.themoviedb.org/3/movie/'
creditsURL2 = '/credits?api_key=85a6946564b671a073402f6de8740a69&language=ko-KR'
videoURL1 = 'https://api.themoviedb.org/3/movie/'
videoURL2 = '/videos?api_key=85a6946564b671a073402f6de8740a69&language=ko-KR'
imgURL = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'
genre_json = requests.get(genreURL).json()
movies_json=[]
for genre in genre_json['genres']:
    movies_genre={
        "model":"movies.genre",
        "pk":genre['id'],
        "fields":{
            "name":genre['name']
        }
    }
    movies_json.append(movies_genre)
actor_pk=1111
actors_json=[]
title_json={
    'title':[],
    'm_id':[],
}
nations=set()
for i in range(1,11):
    moviesURL=f'{movieURL}&page={i}'
    tmp_json=requests.get(moviesURL).json()
    print(moviesURL)
    for result in tmp_json['results']:
        nations.add(result['original_language'])
        poster_path=result['poster_path']
        real_poster_path=f'{imgURL}{poster_path}'
        id=result['id']
        creditsURL=f'{creditsURL1}{id}{creditsURL2}'
        credits_json=requests.get(creditsURL).json()
        actors=[]
        maxIdx=12 if len(credits_json['cast'])>=12 else len(credits_json['cast'])

        for j in range(maxIdx):
            actors.append(actor_pk)
            tmp_path=credits_json['cast'][j]['profile_path']
            movies_actor={
                "model":"movies.actor",
                "pk":actor_pk,
                "fields":{
                    'name':credits_json['cast'][j]['name'],
                    'profile_path':f'{imgURL}{tmp_path}',
                    'character':credits_json['cast'][j]['character']
                }
            }
            actor_pk+=1
            actors_json.append(movies_actor)
        videoURL=f'{videoURL1}{id}{videoURL2}'
        video_json=requests.get(videoURL).json()
        video_path=str(),
        if len(video_json['results'])>0:
            video_path='https://www.youtube.com/embed/'+video_json['results'][0]['key']
        else:
            video_path=""
        movies_movie={
            "model":"movies.movie",
            "fields":{
                'm_id':result['id'],
                'adult' : result['adult'],
                'poster_path':real_poster_path,
                'title':result['title'],
                'overview':result['overview'],
                'nation': result['original_language'],
                'vote_average':result['vote_average'],
                'release_date':result['release_date'],
                'video_path':video_path,
                'genres':result['genre_ids'],
                'actors':actors,
            }
        }
        movies_json.append(movies_movie)
        title_json['title'].append(result['title'])
        title_json['m_id'].append(result['id'])
for actor_json in actors_json:
    movies_json.append(actor_json)
print(nations)
# with open('movies.json','w',encoding='UTF8') as make_file :
#     json.dump(movies_json,make_file,ensure_ascii=False,indent="\t")

with open('title.json','w',encoding='UTF8') as make_file :
    json.dump(title_json,make_file,ensure_ascii=False,indent="\t")