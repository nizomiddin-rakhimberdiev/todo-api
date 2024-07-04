from datetime import datetime
from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    done = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(default=datetime.now)
    updated_at = serializers.DateTimeField(default=datetime.now)


class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'done', 'created_at', 'updated_at')
