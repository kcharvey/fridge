from rest_framework import viewsets

from .models import Food, Recipe
from .serializers import FoodSerializer, RecipeSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows food in the fridge to be viewed or edited
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

