from rest_framework import serializers
from .models import Actor,Movie,Genre
from comments.serializers import CommentSerializer

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Actor
        fields=('name','profile_path','character')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields=('name',)


class MovieSerializer(serializers.ModelSerializer):
    genres=GenreSerializer(many=True,read_only=True)
    actors=ActorSerializer(many=True,read_only=True)
    comments=CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Movie
        fields = (
            'm_id',
            'adult',
            'poster_path',
            'title',
            'overview',
            'nation',
            'vote_average',
            'comment_score_sum',
            'comment_score_average',
            'release_date',
            'video_path',
            'genres',
            'actors',
            'comments',
            'like_users',
        )