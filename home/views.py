from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
# from .serializers import RestaurantSerializer
from .serializer import RestaurantInfoSerializer
# Create your views here.
class RestaurantNameView(APIView):
    def get(self, request):
        # restaurant = Restaurant.objects.first()
        info = RestaurantInfo.objects.first()

        if info:
            serializer = RestaurantInfoSerializer(info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                "name": getattr(settings, "RESTAURANT_NAME", "Default Restaurant"),
                "description": "Welcome to our restaurant! More deatails coming soon ",
                "image": None
            }, status=status.HTTP_200_OK)
        # return Response({"name": settings.RESTAURANT_NAME}, status=status.HTTP_200_OK
    

    def homepage(request):
        info = RestaurantInfo.objects.first()
        if info:
            phone_number = info.phone_number
        else:
            phone_number = getattr(settings, " RESTAURANT_PHONE", "Not Available")
        context={
            "restaurant_phone": phone_number
        }

        return render(request, "home/index.html", context)
    def contact_us(request):
        context = {
            "restaurant_name":"My Restaurant",
            "phone":"+91 1234567890",
            "email":"contact@myrestaurant.com",
            "address": "123 Main Street, HYD, India"

        }
        return render(request, "home/contact_us.html", context)
    