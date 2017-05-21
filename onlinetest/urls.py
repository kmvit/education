from .views import *
from django.conf.urls import include, url
from .models import Quiz, Question, Score

urlpatterns = [
    url(r'^$', index, name='onlinetestlist'),
    url(r'^(?P<quiz_id>\d+)/$', detail),
    url(r'^(?P<quiz_id>\d+)/results/$', results),
    url(r'^(?P<quiz_id>\d+)/do/$',do),
]