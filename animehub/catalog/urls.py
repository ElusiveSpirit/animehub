from django.urls import path

from . import views

urlpatterns = [
    path('animes/', views.AnimeListView.as_view()),
    path('animes/<slug:slug>/', views.AnimeRetrieveView.as_view()),
    path('animes-video/<int:pk>/', views.VideoRetrieveView.as_view()),
    path('animes-video-src/<int:pk>/', views.VideoSourceRetrieveView.as_view()),
]
