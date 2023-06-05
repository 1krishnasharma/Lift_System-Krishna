"""Viewset class for Elevator model."""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from core.models import Elevator
from core.serializers import ElevatorSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    """Viewset class for Elevator model."""

    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

