from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.main),
    url(r'^/processadd$', views.processadd),
    url(r'^/show/(?P<id>\d+)$', views.show),
    url(r'^/delete/(?P<id>\d+)$', views.delete),
    url(r'^/edit/(?P<id>\d+)$', views.edit),
    url(r'^/updateuser/(?P<id>\d+)$', views.updateuser),
    url(r'^/createlike$', views.createlike),
    
    
]