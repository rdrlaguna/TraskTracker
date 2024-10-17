from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from core.models import Category
from core.serializers import CategorySerializer

class MyView(APIView):
    def get(self, request):
        return Response({"text": "Hello Omi"})
    
    def post(self, request, *args, **kwargs):
        print(dir(request))
        return Response(data = {"message": "Objeto creado"}, status=status.HTTP_201_CREATED)


class CategoryViewSet(viewsets.ModelViewSet):

    model = Category
    serializer_class = CategorySerializer
    
    queryset = Category.objects.all()


# TODO: Create Tasks view and serializer. Add to URL paths.
# Solve foreing key issues, Motherfucker!