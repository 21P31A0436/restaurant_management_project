from django.urls import path
from .views import RestaurantNameView

urlpatterns = [
    # path('restaurant/', RestaurantNameView.as_view(), name='restaurant-name'),
    path('', name=)
    path('restaurant-info/', RestaurantInfoView.as_view(), name='restaurant-info'),
    
]