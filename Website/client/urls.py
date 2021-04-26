from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('place-request', views.place_request, name='place_request')
]