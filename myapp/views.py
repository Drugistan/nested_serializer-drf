from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import *
from rest_framework.response import Response
from .serailizer import ProfileSerializer



class ProfileView(APIView):

    def get(self, request):
        instance = Profile.objects.all()
        serializer = ProfileSerializer(instance, many=True)
        if serializer:
            return Response({"response" : serializer.data})
        return Response(serializer.errors)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    def put(self, request, id=None, format=None):
        instance = Profile.objects.get(pk=id)
        serializer = ProfileSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'data': serializer.data
        }
        return response