from django.urls import path
from . import views

urlpatterns = [
    path('wanted/', views.wanted),
    path('highScore/', views.highScore),
    path('animation/', views.animation),
    path('comedyRomance/', views.comedyRomance),
    path('horror/', views.horror),
    path('scienceFiction/', views.scienceFiction),
    path('documentary/',views.documentary),
    path('nation/', views.nation),
    path('sun/', views.sun),
    path('cloud/', views.cloud),
    path('rain/', views.rain),
    path('snow/', views.snow),
    path('detail/<int:movie_id>/',views.movieDetail),
    path('detail/<int:movie_id>/like/', views.movieLike),
]
