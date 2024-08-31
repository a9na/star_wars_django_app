from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.character_list, name='character_list'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
    path('planets/', views.planet_list, name='planet_list'),
    path('starships/', views.starship_list, name='starship_list'),
]
