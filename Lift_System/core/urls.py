from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.viewsets import ElevatorSystemViewSet
router = DefaultRouter()
router.register(r'elevator-systems', ElevatorSystemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]