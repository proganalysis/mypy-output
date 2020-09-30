from django.http import JsonResponse as JsonResponse
from rest_framework import serializers
from typing import Any

class GameSerializer(serializers.Serializer):
    name: Any = ...
    status: Any = ...
    settings: Any = ...
    def get_settings_as_dict(self, game: Any): ...
    def update(self, instance: Any, validated_data: Any): ...