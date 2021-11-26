from django.urls import path, reverse_lazy
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home-view'),
]

