from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from core.models import Elevator, ElevatorRequest
from core.serializers import ElevatorRequestSerializer


class ElevatorRequestViewSet(viewsets.ModelViewSet):
    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer

