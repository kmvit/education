from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', MaterialList.as_view(), name='material_list'),
    url(r'^(?P<pk>\d+)/$', MaterialDetail.as_view(), name='material_detail'),
]
