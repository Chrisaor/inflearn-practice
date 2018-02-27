from django.urls import path

from vote import views

app_name = 'vote'
urlpatterns = [
    path('', views.index, name = 'index')
]