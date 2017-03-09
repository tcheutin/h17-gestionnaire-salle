from django.shortcuts import render

from api.models import Terminal
from api.serializers import TerminalSerializer

from datetime import datetime
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from django.contrib.auth.models import User, Group


class TerminalList(APIView):
    """
    API endpoint that allows PI to be added.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer

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
