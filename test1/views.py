from django.shortcuts import render, get_object_or_404
from rest_framework import  viewsets
from rest_framework.decorators import api_view
from .models import demo
from .serializers import demoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
# Create your views here.


class demoViewSet(viewsets.ModelViewSet):
    """
    API ebdpoint that allows users to be viewed or edited
    """
    # 将左右模型进行降序排列order_by('-age'),所有查询objects.all()
    queryset = demo.objects.all().order_by('age')
    # 序列化器
    serializer_class = demoSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class loginView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        return Response({"status":True})
