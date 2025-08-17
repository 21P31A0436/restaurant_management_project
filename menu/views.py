from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MenuItemView(APIView):
    def get(self, request):
        menu_items =[
            {"id":1, "name": "veg Biryani", "price": 150},
            {"id":2, "name":"paneer Butter Masala", "price":180}
            {"id"3, "name":"Chicken", "price": 200}
        ]
        return Response(menu_items, status=status.HTTP_200_OK)
    def home(request):
        context = {
            "restaurant_name": "SpiceHub Restaurant"
        }
        return render(request, "home.html", context)