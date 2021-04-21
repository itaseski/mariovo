from django.urls import path
from . import views


app_name = 'vilages'
urlpatterns = [
    path('', views.index, name='index'),    
]
