from rest_framework import serializers
from .models import Auditorium

class AuditoriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditorium
        fields = ('id', 'creator_id', 'name', 'address', 'city', 'province', 'capacity')
    