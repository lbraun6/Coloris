"""Coloris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings


def home_view(request):
    print("Home view reached")
    return render(request, "home_template.html")


def about_view(request):

    return render(request, "about_template.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home_view"),
    path("home/", home_view, name="home_view"),
    path("about/", about_view, name="about_view"),
    path("game/", include("color_is.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

