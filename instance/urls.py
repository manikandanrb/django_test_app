from django.urls import path
from instance import views

urlpatterns = [
    path('', views.index),
]
