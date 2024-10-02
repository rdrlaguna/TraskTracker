from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyView(APIView):
    def get(self, request):
        return Response({"text": "Hello Omi"})
    
    def post(self, request, *args, **kwargs):
        print(dir(request))
        return Response(data = {"message": "Objeto creado"}, status=status.HTTP_201_CREATED)

