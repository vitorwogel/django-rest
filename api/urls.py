from django.urls import path
from . import views

urlpatterns = [
    path('getItems/', views.getItems),
    path('addItem/', views.addItem),
    path('deleteItems/', views.deleteItems),
    path('getPersons/', views.getPersons),
    path('addPerson/', views.addPerson),
    path('deletePersons/', views.deletePersons),
]