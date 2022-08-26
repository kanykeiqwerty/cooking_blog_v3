
# from dataclasses import fields
from rest_framework import serializers
from . models import Recipe
from django.db.models import Avg


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=('title', 'image')

    def to_representation(self, instance):
        repr= super().to_representation(instance)
        repr['rating']=instance.reviews.aggregate(Avg('rating'))['rating__avg']
    


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields='__all__'



    def to_representation(self, instance):
        repr= super().to_representation(instance)
        repr['rating']=instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['reviews']=instance.reviews.count()
        return repr

