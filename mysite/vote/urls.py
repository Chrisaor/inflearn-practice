from django.urls import path

from vote import views

app_name = 'vote'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/results/ ', views.results, name = 'result'),
    path('<int:pk>/vote/', views.vote, name = 'vote'),
]