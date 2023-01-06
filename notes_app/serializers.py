from rest_framework import serializers
from .models import Note


# serializers.ModelSerializer just tells django to convert sql to JSON
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note  # tell django which model to use
        fields = ('id', 'notes',)  # tell django which fields to include
