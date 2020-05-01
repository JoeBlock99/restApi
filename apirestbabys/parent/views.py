from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from baby.models import Baby
from baby.serializers import BabySerializer

from parent.models import Parent
from parent.serializers import ParentSerializer

from django.contrib.auth.models import User

# Create your views here.


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    baby_serializer = BabySerializer

    def perform_create(self, serializer):
        parent = serializer.save()
        user = self.request.user
        return Response(serializer.data)

    @action(detail=True, url_path='baby', methods=['get'])
    def baby(self, request, pk=None):
        babies = Baby.objects.all().filter(parent=pk)
        return Response(BabySerializer(babies, many=True).data)
