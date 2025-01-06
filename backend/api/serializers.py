"""serializers."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """class."""

    class Meta:
        """Meta_class."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
