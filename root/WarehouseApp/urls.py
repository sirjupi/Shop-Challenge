from django.urls import re_path
from WarehouseApp import views

from django.conf.urls.static import static

urlpatterns = [

    re_path(r'^warehouse$', views.warehouseApi),
    re_path(r'^warehouse/([0-9]+)$', views.warehouseApi),

    re_path(r'^inventory$', views.inventoryApi),
    re_path(r'^inventory/([0-9]+)$', views.inventoryApi),


]
