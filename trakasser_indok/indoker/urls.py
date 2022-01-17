from django.urls import path
from . import views

app_name = 'indoker'

urlpatterns = [
    path('', views.indoker_list, name="list"),
    path('create/', views.indoker_add, name="create"),
    path('<slug:slug>/', views.indoker, name="detail"),
]