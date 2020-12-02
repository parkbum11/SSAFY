from . import views
from django.urls import path

app_name = 'community'
urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('new_review/', views.new_review, name='new_review'),
    path('review_detail/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('create', views.create, name='create'),
]