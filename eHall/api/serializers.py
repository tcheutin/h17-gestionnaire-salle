# from django.contrib.auth.models import User, Group
from api.models import Terminal
from rest_framework import serializers


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ('token', 'ipAddress', 'status')
