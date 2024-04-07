from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_home, name="food_home"),
    path('sales/', views.sales, name="sales"),
    path('waste/', views.waste, name="waste"),
    path('ordering/', views.ordering, name="ordering"),
]