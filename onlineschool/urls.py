from django.conf.urls import url, include
from django.contrib import admin
from materials.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^material/', include('materials.urls', namespace='materiallist', app_name='material')),
    url(r'^quiz/',  include('onlinetest.urls', namespace='quiz', app_name='onlinetest')),
    url(r'^$', Home.as_view(), name='home')
]
