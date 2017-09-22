from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='templates/index.html'),
    url(r'^templates/', TemplateView.as_view(template_name="d3.html"),
                   name='views'),
    url(r'^submit/$', views.submit, name='submit')
]