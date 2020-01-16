from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from mainapp.models import Note
from mainapp.serializers import NoteSerializer
from mainapp.models import DBItem
from mainapp.serializers import dbItemSerializer



import json

class NoteViewSet(viewsets.ModelViewSet):
    #check permissions
    permission_classes={
        IsAuthenticated,
    }
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field ="id"

class DBItemViewSet(viewsets.ModelViewSet):
    #check permissions
    permission_classes={
        IsAuthenticated,
    }
    queryset = DBItem.objects.all()
    serializer_class = dbItemSerializer
    lookup_field ="id"











