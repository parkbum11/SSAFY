from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
    )
    movie_title = forms.CharField(
        label='영화제목',
    )
    content = forms.CharField(
        label='내용',
    )
    rank = forms.IntegerField(
        label='rank',
    )
    class Meta:
        model = Review
        fields = '__all__'