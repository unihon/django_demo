from django.urls import path
from . import views

urlpatterns = [
    path('', views.Apple.as_view()),
    path('apple', views.Apple.as_view()),
    path('sydney', views.Sydney.as_view()),
]
