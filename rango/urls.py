from django.conf.urls import url, patterns
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index')
)

