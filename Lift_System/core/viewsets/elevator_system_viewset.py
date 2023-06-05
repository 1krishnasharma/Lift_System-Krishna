"""Viewset for ElevatorSystem"""
from django.db.models import F, Func

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.serializers import ElevatorSystemSerializer, ElevatorRequestSerializer
from core.models import ElevatorSystem, Elevator


class ElevatorSystemViewSet(viewsets.ModelViewSet):
    """Viewset for ElevatorSystem"""

    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

