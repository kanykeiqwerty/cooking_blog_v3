from multiprocessing import context
from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet

from rating.serializers import ReviewSerializer
from . import serializers
from . models import Recipe
from rest_framework.decorators import action



class ProductViewSet(ModelViewSet):
    queryset=Recipe.objects.all()
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]



    def get_serializer_class(self):
        if self.action=='list':
            return serializers.RecipeListSerializer

        return serializers.RecipeDetailSerializer

    #api/v1/products/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk=None):
        recipe=self.get_object()
        if request.method=='GET':
            reviews=recipe.reviews.all()
            serializer=ReviewSerializer(reviews, many=True).data
            return response.Response(serializer, status=200)
        data=request.data
        serializer=ReviewSerializer(data=data, context={'request':request, 'recipe':recipe})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201)


