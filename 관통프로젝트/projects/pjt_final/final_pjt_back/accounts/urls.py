from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.Signup),
    path('profile/<str:username>/', views.Profile),
    path('api-token-auth/', obtain_jwt_token),
]
