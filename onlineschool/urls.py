from django.conf.urls import url, include
from django.contrib import admin
from materials.views import *
from .settings import STATIC_ROOT
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^material/', include('materials.urls', namespace='materiallist', app_name='material')),
    url(r'^test/',  include('quiz.urls', namespace='quiz', app_name='quiz')),
    url(r'^$', Home.as_view(), name='home')
]
