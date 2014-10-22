from rest_framework import serializers

from .models import Food, Recipe


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('name', 'quantity', 'unit')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'ingredients')

