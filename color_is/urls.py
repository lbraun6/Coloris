from django.urls import path

from . import views

app_name = 'color_is'
urlpatterns = [
    path("play/", views.game_view, name="game_view"),
    path("evaluate_guess/", views.evaluate_guess_view, name="evaluate_guess_view"),
    path("final_score/", views.final_score_view, name="final_score_view"),
    path("score/", views.score_view, name="score_view"),
]
