from rest_framework import serializers
from .models import Comment,coComment

class CoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=coComment
        fields=('id','username','content','created_at')


class CommentSerializer(serializers.ModelSerializer):
    co_comment=CoCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields=(
            'id',
            'username',
            'title',
            'content',
            'score',
            'created_at',
            'like_users',
            'hate_users',
            'co_comment',
        )
