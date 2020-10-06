from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:movie_id>/', views.details, name='details'),
    path('add_movie', views.add_movie, name='add_movie'),
    path('edit_movie/<int:movie_id>/', views.edit_movie, name="edit_movie"),
]
