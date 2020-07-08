from django.conf.urls import url
from pokemon import views

urlpatterns = [
    url(r'^api/pokemon$', views.find_by_name),
    url(r'^api/pokemon/find/all$', views.find_all),
    url(r'^api/pokemon/tipo/find/all$', views.find_tipo_all),
    url(r'^api/pokemon/find/(?P<pk>[0-9]+)$', views.find_by_id),
    url(r'^api/pokemon/create$', views.create),
    url(r'^api/pokemon/update/(?P<pk>[0-9]+)$', views.update),
    url(r'^api/pokemon/delete/(?P<pk>[0-9]+)$', views.delete),
    url(r'^api/pokemon/remove/all$', views.delete_all),
]

