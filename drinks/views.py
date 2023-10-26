from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# GET Request Function

@api_view(["GET", "POST"])
def drink_list(request):

    # Get all the items, serialize them and return them as JSON

    if request.method == "GET":
        drinks = Drink.objects.all() # Takes al lthe items
        serializer = DrinkSerializer(drinks, many=True) # Serializes the items fro mthe list
        return JsonResponse({"drinks": serializer.data}) # set: safe=False, if no object exists
    
    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)