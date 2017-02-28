from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^products_main$', views.products_main),
    url(r'^product_spotlight$', views.product_spotlight),
    url(r'^shopping_cart$', views.shopping_cart),

]
