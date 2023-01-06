from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import NoteSerializer
from .models import Note



class NoteList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Note.objects.all().order_by('id')
    serializer_class = NoteSerializer  # tell django what serializer to use


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all().order_by('id')
    serializer_class = NoteSerializer


