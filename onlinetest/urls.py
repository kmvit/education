from .views import *
from django.conf.urls import include, url
from .models import *

urlpatterns = [
    url(r'^$', TestList.as_view(), name='test_list'),
    url(r'^(?P<pk>\d+)/$', TestDetail.as_view(), name='test_detail'),
    url(r'^(?P<pk>\d+)/(?P<question_pk>\d+)/$', QuestionDetail.as_view(), name='question_detail'),
]

