from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from .serializers import RestaurantSerializer
# Create your views here.
class RestaurantNameView(APIView):
    def get(self, request):
        restaurant = Restaurant.objects.first()
        if restaurant:
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"name": settings.RESTAURANT_NAME}, status=status.HTTP_200_OK)

