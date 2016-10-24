from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<model_name>[^/]+)/(?P<page_id>[0-9]+)/$', views.similar_image, name='sim'),
    # url(r'^(?P<image>.+)/modify/$', views.modify, name='modify'),
    url(r'^export/$', views.export, name='export'),
]
