from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='test/index.html'),
    url(r'^submit/$', views.submit, name='submit')
]