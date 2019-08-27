from django.urls import path

from . import views

urlpatterns = [
    path('animes/', views.AnimeListView.as_view()),
    path('animes/<slug:slug>/', views.AnimeRetrieveView.as_view()),
]
