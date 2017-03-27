from django.shortcuts import render

from api.models import Terminal
from api.serializers import TerminalSerializer, TicketSerializer, ReportSerializer, ClosingSerializer
from eHall.models import Ticket
from report.models import Report as ReportModel
from event.models import Event

from datetime import datetime
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TerminalList(APIView):
    """
    API endpoint that allows PI to be listed and added.
    """

    def get(self, request, format=None):
        terminals = Terminal.objects.all()
        serializer = TerminalSerializer(terminals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TerminalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketList(APIView):
    """
    API endpoint that allow PI to get the ticket list.
    """

    def get(self, request, format=None):
        # TODO : Add check if event ready to be check
        address = request.META.get('HTTP_IPADDRESS')
        if address is not None:

            terminal = Terminal.objects.raw(
                'SELECT * FROM api_terminal WHERE "address"=%s', [address])

            if len(list(terminal)) == 1:
                print("Terminal " + str(terminal[0].address) + " request tickets.")

                events = Event.objects.raw(
                'SELECT * FROM event_event WHERE "id"=%s',
                [terminal[0].event_id])

                if len(list(events)) == 1:
                    if not events[0].isClose:

                        tickets = Ticket.objects.raw(
                            'SELECT * FROM event_ticket WHERE "event_id"=%s',
                            [terminal[0].event_id])
                        if len(list(tickets)) != 0:
                            serializer = TicketSerializer(tickets, many=True)

                            return Response(serializer.data)
                        return Response("No tickets", status=status.HTTP_404_NOT_FOUND)
                    return Response("Event closed", status=status.HTTP_404_NOT_FOUND)
                return Response("No event found", status=status.HTTP_404_NOT_FOUND)
            return Response("No terminal found", status=status.HTTP_404_NOT_FOUND)
        return Response("Missing key in header", status=status.HTTP_400_BAD_REQUEST)

class Report(APIView):
    """
    API endpoint that allow a terminal to send his final report.
    """

    def post(self, request, format=None):
        address = request.META.get('HTTP_IPADDRESS')

        if address is not None:
            t = Terminal.objects.raw(
                'SELECT * FROM api_terminal WHERE "address"=%s', [address])

            report_json = request.data

            for report_dict in report_json:
                terminal = t
                print("terminal " + str(terminal[0].address))

                httpResponse = report_dict.get('httpResponse')
                print("httpResponse: " + httpResponse)

                time = report_dict.get('time')
                print("time: " + time)

                ticketHash = report_dict.get('ticketHash')
                print("ticketHash: " + ticketHash)

                ReportModel.objects.create(terminal=terminal[0],
                                           ticketHash=ticketHash,
                                           httpResponse=httpResponse,
                                           time=time)

            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Close(APIView):
    """
    API endpoint that allow a terminal to know if an event is finish.
    """

    def get(self, request, format=None):
        address = request.META.get('HTTP_IPADDRESS')
        if address is not None:

            terminal = Terminal.objects.raw(
                'SELECT * FROM api_terminal WHERE "address"=%s', [address])

            if str(len(list(terminal))) == "1":
                print("terminal " + str(terminal[0].address))

                events = Event.objects.raw(
                    'SELECT * FROM event_event WHERE "id"=%s',
                    [terminal[0].event_id])

                print("event " + str(events[0].isClose))
                print("Events " + str(len(list(events))))

                if str(len(list(events))) == "1":
                    serializer = ClosingSerializer(events, many=True)

                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response("No event found", status=status.HTTP_404_NOT_FOUND)
            return Response("No terminal found", status=status.HTTP_404_NOT_FOUND)
        return Response("Missing key in header",status=status.HTTP_400_BAD_REQUEST)
