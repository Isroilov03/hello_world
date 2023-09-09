from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('search/', search_view, name='search_url'),
    path('car-detail/<int:pk>/', car_detail_view, name='car_detail_url')
]
