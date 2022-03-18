from django.shortcuts import render, get_object_or_404
from rest_framework import  viewsets
from rest_framework.decorators import api_view
from .models import demo
from .serializers import demoSerializer
from rest_framework.response import Response
from rest_framework import status

from test1 import serializers
# Create your views here.


class demoViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = demoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    def update(self, request, pk):
        try:
            old_demo = demo.objects.get(name=pk)
        except demo.DoesNotExist:
            return Response({
                'status': 404,
                'msg': 'NotFound'
            })
        new_demo = serializers.demoSerializer(instance=old_demo,data=request.data,partial=False)
        new_demo.is_valid(raise_exception=True)
        new_demo.save()
        return Response(status=status.HTTP_200_OK)