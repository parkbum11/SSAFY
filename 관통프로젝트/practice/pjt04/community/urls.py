from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.review_list, name='review_list'),
    path('<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('<int:review_pk>/delete/', views.delete, name='delete'),
]

