from api.models import Terminal
from eHall.models import Ticket
from event.models import Event
from auditorium.models import Auditorium
from report.models import Report
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
        fields = ('name', 'startDate', 'auditorium')

## MISSING TIME
# TODO : Add closing time
class TicketSerializer(serializers.ModelSerializer):
    # validationTerminal = TerminalSerializer(read_only=True)
    event = EventSerializer(read_only=True)
    class Meta:
        model = Ticket
        fields = ('id', 'owner', 'event')

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('terminal','httpResponse', 'ticketHash' ,'time')

class ClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'isClose')
