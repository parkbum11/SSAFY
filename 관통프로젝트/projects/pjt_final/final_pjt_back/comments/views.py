from django.shortcuts import get_object_or_404

from .models import Comment,coComment
from movies.models import Movie
from .serializers import CommentSerializer, CoCommentSerializer
from movies.serializers import MovieSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request,movie_id):
    movie=get_object_or_404(Movie,m_id=movie_id)
    if request.method=='GET':
        comments=Comment.objects.order_by('-score').filter(movie=movie)
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
    else:
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,movie=movie,username=request.user.username)
            l=movie.comments.count()
            s=movie.comment_score_sum
            movie.comment_score_sum=s+float(request.data.get('score'))
            movie.comment_score_average=round(movie.comment_score_sum/l,1)
            movie.save()
            m_serializer=MovieSerializer(movie)
            return Response(m_serializer.data)


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_detail_update_delete(request,movie_id,comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)
    movie=get_object_or_404(Movie,m_id=movie_id)
    if request.method=='GET':
        serializer=CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method=='DELETE':
        comment=get_object_or_404(Comment,pk=comment_id)
        if comment.user!=request.user :
            return Response({'error': '권한이 없습니다.'})
        else:
            tmp_score=comment.score
            comment.delete()
            l=movie.comments.count()
            if l>0:
                s=movie.comment_score_sum
                movie.comment_score_sum=s-tmp_score
                movie.comment_score_average=round(movie.comment_score_sum/l,1)
            else:
                movie.comment_score_sum=0
                movie.comment_score_average=0.0
            movie.save()
            serializer=MovieSerializer(movie)
            return Response(serializer.data)
    else:
        l=movie.comments.count()
        s=movie.comment_score_sum-comment.score
        if comment.user!=request.user :
            return Response({'error': '권한이 없습니다.'})
        serializer=CommentSerializer(instance=comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            movie.comment_score_sum=s+float(request.data.get('score'))
            movie.comment_score_average=round(movie.comment_score_sum/l,1)
            movie.save()
            m_serializer=MovieSerializer(movie)
            return Response(m_serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_like(request,movie_id,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)
    movie=get_object_or_404(Movie, m_id=movie_id)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_hate(request,movie_id,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)
    movie=get_object_or_404(Movie, m_id=movie_id)
    if comment.hate_users.filter(pk=request.user.pk).exists():
        comment.hate_users.remove(request.user)
    else:
        comment.hate_users.add(request.user)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def co_comment_create(request,movie_id,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)
    co_serializer=CoCommentSerializer(data=request.data)
    movie=get_object_or_404(Movie, m_id=movie_id)
    if co_serializer.is_valid(raise_exception=True):
        co_serializer.save(user=request.user,comment=comment, username=request.user.username)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def co_comment_delete(request,movie_id,comment_id,co_comment_id):
    co_comment=get_object_or_404(coComment,pk=co_comment_id)
    movie=get_object_or_404(Movie, m_id=movie_id)
    if co_comment.user!=request.user:
        return Response({'error': '권한이 없습니다.'})
    co_comment.delete()
    serializer=MovieSerializer(movie)
    return Response(serializer.data)    