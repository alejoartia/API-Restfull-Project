from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer