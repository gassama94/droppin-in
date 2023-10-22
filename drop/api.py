from drop.models import Drop
from rest_framework import viewsets, permissions
from .serializers import DropSerializer

# Drop Viewset
class DropViewSet(viewsets.ModelViewSet):
  queryset = Drop.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]

  serializer_class = DropSerializer