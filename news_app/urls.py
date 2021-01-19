from django.contrib import admin
from django.urls import path
from news_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.news),
    path('home', views.news, name="home"),
    path('about', views.about, name="about"),
    path('developer', views.developer, name="developer"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)