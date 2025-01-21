# movies/forms.py
from django import forms
from .models import Movie


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date','image_url']

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        # You can customize the form fields here if needed

    # You can add additional form validation or customization methods here if needed

# movies/forms.py


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SignUpForm:
    pass