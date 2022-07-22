from django.urls import path, include

from . import views

app_name = 'webpages'
urlpatterns = [
    path('', views.index, name='index')
]

