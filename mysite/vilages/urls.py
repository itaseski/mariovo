from django.urls import path
from . import views


app_name = 'vilages'
urlpatterns = [
    # ex: /vilages/
    path('', views.index, name='index'),    
]
