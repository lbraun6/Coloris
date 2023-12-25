from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'color_is'
urlpatterns = [
    path("play/", views.game_view, name="game_view"),
    path("evaluate_guess/", views.evaluate_guess_view, name="evaluate_guess_view"),
    path("final_score/", views.final_score_view, name="final_score_view"),
    path("score/", views.score_view, name="score_view"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
