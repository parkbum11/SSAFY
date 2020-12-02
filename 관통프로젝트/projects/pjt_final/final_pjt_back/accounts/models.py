from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
# Create your models here.

class User(AbstractUser):
    isLikedAnimation=models.BooleanField(default=False)
    isLikedComedy=models.BooleanField(default=False)
    isLikedRomance=models.BooleanField(default=False)
    isLikedMusic=models.BooleanField(default=False)
    isLikedDrama=models.BooleanField(default=False)
    isLikedHorror=models.BooleanField(default=False)
    isLikedThriller=models.BooleanField(default=False)
    isLikedCriminal=models.BooleanField(default=False)
    isLikedMistery=models.BooleanField(default=False)
    isLikedSf=models.BooleanField(default=False)
    isLikedWar=models.BooleanField(default=False)
    isLikedAdventure=models.BooleanField(default=False)
    isLikedFantasy=models.BooleanField(default=False)
    isLikedAction=models.BooleanField(default=False)
    isLikedHistory=models.BooleanField(default=False)
    isLikedDocumentary=models.BooleanField(default=False)
    nation=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    likeMovies=models.ManyToManyField(Movie, related_name="like_users", blank=True)