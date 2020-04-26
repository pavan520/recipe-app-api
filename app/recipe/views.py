from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from core.models import Tag, Ingredient, Recipe


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin, mixins.CreateModelMixin):
    """ Base view set for user own recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Return objects for current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """ Creates new object"""
        serializer.save(self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """ Manage tags in the DB"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    """ Manage ingredients in db"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """ Manage recipes in DB"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Retrieve for the authenticated users"""
        return self.queryset.filter(user= self.request.user)
