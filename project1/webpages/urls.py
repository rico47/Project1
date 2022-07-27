from django.urls import path

from . import views

app_name = 'webpages'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.navbar, name='navbar')
]

