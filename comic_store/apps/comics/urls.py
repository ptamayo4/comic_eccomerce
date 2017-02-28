from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin$', views.admin),
    url(r'^dashboard$', views.admin_login),
    url(r'^register$', views.register),
    url(r'^dashboard/products$', views.product_view),
    url(r'^dashboard/orders$', views.orders_view)
]
