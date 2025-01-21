# app's urls.py
from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    UserPageView,
    SignUpView,  # Correct import for SignUpView
    RentMovieView,
    LoginView,
    RentedMoviesView,# Import the LoginView
)

urlpatterns = [
    path('movie-list/', MovieListView.as_view(), name='movie-list'),
    path('movie-detail/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('create-movie/', MovieCreateView.as_view(), name='movie-create'),
    path('update-movie/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('delete-movie/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    path('user-page/', UserPageView.as_view(), name='user-page'),
    path('rent-movie/<int:pk>/', RentMovieView.as_view(), name='rent-movie'),
    path('', LoginView.as_view(), name='login'),  # Use as_view() here for class-based view
    path('signup/', SignUpView.as_view(), name='signup'),  # Use as_view() for SignUpView
    path('rented-movies/', RentedMoviesView.as_view(), name='rented-movies'),
]

