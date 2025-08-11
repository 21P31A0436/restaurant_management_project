from django.urls import path
from .views import *

urlpatterns = [
    # path('restaurant/', RestaurantNameView.as_view(), name='restaurant-name'),
    path('restaurant-info/', RestaurantInfoView.as_view(), name='restaurant-info'),
    
]