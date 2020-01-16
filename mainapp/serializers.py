from rest_framework import serializers

from mainapp.models import Note
from mainapp.models import DBItem
from mainapp.models import Structure


class NoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields ="__all__"

class dbItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = DBItem
		fields = "__all__"

class CreateSerializer(serializers.ModelSerializer):
	class  Meta:
		model =  Structure
		fields = "__all__"

