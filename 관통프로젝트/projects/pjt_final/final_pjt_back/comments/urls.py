from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/', views.comment_list_create),
    path('<int:movie_id>/<int:comment_id>/', views.comment_detail_update_delete),
    path('<int:movie_id>/like/<int:comment_id>/', views.comment_like),
    path('<int:movie_id>/hate/<int:comment_id>/', views.comment_hate),
    path('<int:movie_id>/<int:comment_id>/comment/', views.co_comment_create),
    path('<int:movie_id>/<int:comment_id>/comment/<int:co_comment_id>/', views.co_comment_delete),
]
