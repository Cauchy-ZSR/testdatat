from django.db import router
from django.urls import path, include, re_path
from .views import demoViewSet



urlpatterns = [
    re_path(r'^demo/$', demoViewSet.as_view({'post':'create'})),
    re_path(r'^demo/(?P<pk>\w+)', demoViewSet.as_view({'put':'update'}))
]