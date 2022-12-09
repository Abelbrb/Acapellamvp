from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('create',views.create,name="create"),
    path('<slug:slug>/', views.room, name='room'),
]