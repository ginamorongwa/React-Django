from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import RoomSerializer
from .serializers import Room

class RoomView(generics.ListAPIView):# CreateAPIView): 
    queryset = Room.objects.all() # return all room objects
    serializer_class = RoomSerializer












# from django.http import HttpResponse


# '''
# take in a request
# return a response
# '''
# def main(request):
#     return HttpResponse("<h1>Hello</h1>")
