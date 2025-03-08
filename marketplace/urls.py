from django import views
from django.contrib import admin
from django.urls import include, path

from marketplace.views import ProductView


urlpatterns = [
    path('dashboard/', ProductView.dashboard, name = "dashboard"),
]