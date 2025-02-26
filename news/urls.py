from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_home, name="news"),
    path("crate/", views.create, name="create"),
]