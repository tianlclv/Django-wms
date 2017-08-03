from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^order', views.order, name='order'),
    url(r'^adduser', views.adduser, name='adduser'),
    url(r'^userlist', views.userlist, name='userlist'),
    url(r'^address', views.address, name='address'),
    url(r'^product', views.product, name='product'),

]
