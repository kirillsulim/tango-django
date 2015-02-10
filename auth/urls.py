from django.conf.urls import url, patterns
from auth import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='register'),
)
