# from django.contrib.auth.models import User, Group
from api.models import Terminal
from event.models import Ticket, Event
from auditorium.models import Auditorium
from rest_framework import serializers


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ('address', 'status')

class AuditoriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditorium
        fields = ('name', 'address')

class EventSerializer(serializers.ModelSerializer):
    auditorium = AuditoriumSerializer(read_only=True)
    class Meta:
        model = Event
        fields = ('title', 'auditorium')

## MISSING TIME
class TicketSerializer(serializers.ModelSerializer):
    # validationTerminal = TerminalSerializer(read_only=True)
    event = EventSerializer(read_only=True)
    class Meta:
        model = Ticket
        fields = ('id', 'owner', 'event')
