from django.urls import path
from . import views

urlpatterns = [
    path('', views.Apple.as_view()),
    path('object', views.Sydney.as_view()),
]
