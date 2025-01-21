# movies/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Rental
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MovieForm, CustomUserCreationForm
import logging

logger = logging.getLogger(__name__)  # Create a logger instance

class SignUpView(View):
    template_name = 'movies/signup.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info(f"User {user.username} signed up and logged in successfully.")  # Log the successful signup and login
            return redirect('user-page')
        else:
            logger.error(f"Error during user signup: {form.errors}")  # Log the form errors
            messages.error(request, 'Registration failed. Please correct the errors in the form.')
        return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'movies/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user_type == 'admin' and user.is_staff:
                login(request, user)
                return redirect('movie-list')
            elif user_type == 'user' and not user.is_staff:
                login(request, user)
                return redirect('user-page')
            else:
                messages.error(request, 'Invalid user type.')
        else:
            messages.error(request, 'Invalid login credentials.')

        return render(request, self.template_name)


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


class MovieCreateView(View):
    template_name = 'movies/create_movie.html'

    def get(self, request):
        form = MovieForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        return render(request, self.template_name, {'form': form})


class MovieUpdateView(View):
    template_name = 'movies/update_movie.html'

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(instance=movie)
        return render(request, self.template_name, {'form': form, 'movie': movie})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        return render(request, self.template_name, {'form': form, 'movie': movie})


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie-list')


# views.py
class UserPageView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movies/user_page.html'
    context_object_name = 'movies'


class RentMovieView(LoginRequiredMixin, View):
    template_name = 'movies/rent_movie.html'

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)

        if movie.is_rented():
            return render(request, self.template_name, {'movie': movie, 'message': 'Movie is already rented.'})

        return render(request, self.template_name, {'movie': movie, 'message': None})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)

        if not movie.is_rented():
            Rental.objects.create(movie=movie, rented_by=request.user)
            # Redirect to a view that shows all rented movies
            return redirect('rented-movies')  # Assuming you have a view named 'rented-movies'
        else:
            return render(request, self.template_name, {'movie': movie, 'message': 'Movie is already rented.'})

# views.py

from django.shortcuts import render
from django.views import View
from .models import Rental

class RentedMoviesView(View):
    template_name = 'movies/rented_movies.html'

    def get(self, request):
        rented_movies = Rental.objects.select_related('movie', 'rented_by').all()
        return render(request, self.template_name, {'rented_movies': rented_movies})
