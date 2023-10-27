from django.http import HttpResponse, JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request, format=None):
    return HttpResponse("Home Page is Under Construction!")

# GET Request Function

@api_view(["GET", "POST"])
def drink_list(request, format=None):

    # Get all the items, serialize them and return them as JSON

    if request.method == "GET":
        drinks = Drink.objects.all() # Takes al lthe items
        serializer = DrinkSerializer(drinks, many=True) # Serializes the items fro mthe list
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method == "DELETE":
        drink.delete()
        return Response(stauts=status.HTTP_204_NO_CONTENT)