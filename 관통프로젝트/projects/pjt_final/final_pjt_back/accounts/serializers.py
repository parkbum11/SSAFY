from rest_framework import serializers
from django.contrib.auth import get_user_model
from comments.serializers import CommentSerializer
from movies.serializers import MovieSerializer

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    comments=CommentSerializer(many=True, read_only=True)
    likeMovies=MovieSerializer(many=True, read_only=True)
    class Meta:
        model=get_user_model()
        fields=(
            'username',
            'email',
            'password',
            'nation',
            'age',
            'gender',
            'isLikedAnimation',
            'isLikedComedy',
            'isLikedRomance',
            'isLikedMusic',
            'isLikedDrama',
            'isLikedHorror',
            'isLikedThriller',
            'isLikedCriminal',
            'isLikedMistery',
            'isLikedSf',
            'isLikedWar',
            'isLikedAdventure',
            'isLikedFantasy',
            'isLikedAction',
            'isLikedHistory',
            'isLikedDocumentary',
            'comments',
            'likeMovies',
        )