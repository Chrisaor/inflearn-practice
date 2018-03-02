from django.conf.urls import url

from kilogram import views

app_name = 'kilogram'
urlpatterns = [
    url('', views.Index, name = 'index'),

]