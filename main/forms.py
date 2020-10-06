from django.forms import ModelForm
from .models import Movie

class AddMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'director', 'cast', 'description', 'release_date', 'image']