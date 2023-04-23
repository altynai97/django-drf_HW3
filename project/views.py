from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from .models import Category, Company, Product
from .serializers import CategorySerializer, CompanySerializer, ProductSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        if set(request.data['name']) & set('!@#$%^&*'):
            raise ValidationError('наименование фирмы не могут содержать специальных символов')
        return super().create(request, *args, **kwargs)


class CategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def update(self, request, *args, **kwargs):
        if set(request.data['name']) & set('!@#$%^&*'):
            raise ValidationError('наименование фирмы не могут содержать специальных символов')
        return super().update(request, *args, **kwargs)


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        if set(request.data['name']) & set('!@#$%^&*'):
            raise ValidationError('наименование фирмы не могут содержать специальных символов')
        return super().create(request, *args, **kwargs)


class CompanyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def update(self, request, *args, **kwargs):
        if set(request.data['name']) & set('!@#$%^&*'):
            raise ValidationError('наименование фирмы не могут содержать специальных символов')
        return super().update(request)

