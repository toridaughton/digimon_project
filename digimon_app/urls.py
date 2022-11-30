from django.urls import include, path
from digimon_app import views

urlpatterns = [
    path('', views.index, name='index'),
]