from . import views
from django.urls import path

urlpatterns = [
    path('', views.partners, name="partners_home"),
]