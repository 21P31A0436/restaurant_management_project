from django.urls import path
from .views import home,MenuItemView,reservations

urlpatterns = [
    path('', home, name="home"),
    path('menu-items/', MenuItemView.as_view(), name="menu-items"),
    path('reservations/', reservations, name="reservations"),
]