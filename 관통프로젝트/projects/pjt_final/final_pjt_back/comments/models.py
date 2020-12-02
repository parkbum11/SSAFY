from django.db import models
from django.conf import settings
from movies.models import Movie
# Create your models here.

class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments", blank=True)
    username=models.CharField(max_length=50, blank=True)
    title=models.TextField()
    content=models.CharField(max_length=100)
    score=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)
    hate_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_comments', blank=True)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments", blank=True)


class coComment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="co_comments", blank=True)
    username=models.CharField(max_length=50, blank=True)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="co_comment", blank=True)
    content=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)