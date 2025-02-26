from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("water/", views.water, name="water"),
    path("forests/", views.forests, name="forests"),
    path("deserts/", views.deserts, name="deserts"),
]