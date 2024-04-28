from . import views
from django.urls import path

urlpatterns = [
    path('', views.analytics, name="analytics_home"),
]