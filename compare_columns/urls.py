from django.contrib import admin
from django.urls import path

from . import views

#app_name=compare_columns

urlpatterns = [
    path("", views.About.as_view(), name="about"),
    path('audrey', views.Audrey.as_view(), name="audreyview"),
    path('susan', views.Susan.as_view(), name="susanview"),
]
