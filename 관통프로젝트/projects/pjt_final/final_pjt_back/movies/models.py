from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Actor(models.Model):
    name=models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200)
    character = models.CharField(max_length=100)


class Movie(models.Model):
    m_id=models.IntegerField()
    adult=models.BooleanField()
    poster_path=models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    overview=models.TextField()
    nation=models.CharField(max_length=50)
    vote_average = models.FloatField()
    comment_score_sum=models.IntegerField(default=0)
    comment_score_average=models.FloatField(default=0)
    release_date = models.DateField()
    video_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)

    def __str__(self):
        return self.title
    
