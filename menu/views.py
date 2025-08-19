from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MenuItemView(APIView):
    
    def get(self, request):
        try:
            menu_items =[
                {"id":1, "name": "veg Biryani", "price": 150},
                {"id":2, "name":"paneer Butter Masala", "price":180}
                {"id"3, "name":"Chicken", "price": 200}
            ]
            return Response(menu_items, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error":"Something went wrong while fetching menu items","details":str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    def home(request):
        context = {
            "restaurant_name": "SpiceHub Restaurant"
        }
        return render(request, "home.html", context)
    # def django.shortcuts import render
    def reservations(request):
        return render(request, "reservations.html")
    
