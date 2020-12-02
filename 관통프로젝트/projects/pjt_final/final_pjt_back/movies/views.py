from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Movie,Actor,Genre
from .serializers import MovieSerializer
from accounts.serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from django.db.models import Q 
# Create your views here.

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def wanted(request):
    u_serializer=UserSerializer(request.user)
    movies=Movie.objects.none()
    if request.user.isLikedAnimation:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=16))
        else:
            movies = movies.union(Movie.objects.filter(genres=16, adult=False))
    if request.user.isLikedComedy:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=35))
        else:
            movies = movies.union(Movie.objects.filter(genres=35, adult=False))
    if request.user.isLikedRomance:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=10749))
        else:
            movies = movies.union(Movie.objects.filter(genres=10749, adult=False))
    if request.user.isLikedMusic:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=10402))
        else:
            movies = movies.union(Movie.objects.filter(genres=10402, adult=False))
    if request.user.isLikedDrama:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=18))
        else:
            movies = movies.union(Movie.objects.filter(genres=18, adult=False))
    if request.user.isLikedHorror:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=27))
        else:
            movies = movies.union(Movie.objects.filter(genres=27, adult=False))
    if request.user.isLikedThriller:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=53))
        else:
            movies = movies.union(Movie.objects.filter(genres=53, adult=False))
    if request.user.isLikedCriminal:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=80))
        else:
            movies = movies.union(Movie.objects.filter(genres=80, adult=False))
    if request.user.isLikedMistery:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=9648))
        else:
            movies = movies.union(Movie.objects.filter(genres=9648, adult=False))
    if request.user.isLikedSf:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=878))
        else:
            movies = movies.union(Movie.objects.filter(genres=878, adult=False))
    if request.user.isLikedWar:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=10752))
        else:
            movies = movies.union(Movie.objects.filter(genres=10752, adult=False))
    if request.user.isLikedAdventure:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=12))
        else:
            movies = movies.union(Movie.objects.filter(genres=12, adult=False))
    if request.user.isLikedFantasy:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=14))
        else:
            movies = movies.union(Movie.objects.filter(genres=14, adult=False))
    if request.user.isLikedAction:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=28))
        else:
            movies = movies.union(Movie.objects.filter(genres=28, adult=False))
    if request.user.isLikedHistory:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=36))
        else:
            movies = movies.union(Movie.objects.filter(genres=36, adult=False))
    if request.user.isLikedDocumentary:
        if u_serializer.data['age']>=20:
            movies = movies.union(Movie.objects.filter(genres=99))
        else:
            movies = movies.union(Movie.objects.filter(genres=99, adult=False))
    movies=movies.order_by('-vote_average')[:18]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def highScore(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies=Movie.objects.order_by('-comment_score_average')[:18]
    else:
        movies=Movie.objects.order_by('-comment_score_average').filter(adult=False)[:18]
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def animation(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies=Movie.objects.order_by('-vote_average').filter(genres=16)[:18]
    else:
        movies=Movie.objects.order_by('-vote_average').filter(genres=16, adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comedyRomance(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(35,10749,10402,18))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(35,10749,10402,18), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def horror(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(27,53,80,9648))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(27,53,80,9648), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def scienceFiction(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(878,10752,12,14,28))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(878,10752,12,14,28), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def documentary(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(36,99))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(36,99), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def nation(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies=Movie.objects.order_by('-vote_average').filter(nation=request.user.nation)[:18]
    else:
        movies=Movie.objects.order_by('-vote_average').filter(nation=request.user.nation, adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def sun(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(878,28))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(878,28), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def cloud(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(10749,10402,18))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(10749,10402,18), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rain(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(27,53,80))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(27,53,80), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def snow(request):
    u_serializer=UserSerializer(request.user)
    if u_serializer.data['age']>=20:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(18))[:18]
    else:
        movies = Movie.objects.order_by('-vote_average').filter(genres=(18), adult=False)[:18]
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movieDetail(request,movie_id):
    movie=get_object_or_404(Movie,m_id=movie_id)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movieLike(request,movie_id):
    movie=get_object_or_404(Movie, m_id=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)