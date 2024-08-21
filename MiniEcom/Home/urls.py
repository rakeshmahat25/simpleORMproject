from django.urls import path

from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:customer_id>/product/add/', views.add_product, name='add_product'),
    path('customer/<int:customer_id>/edit/', views.edit_customer, name='edit_customer'),
    path('customer/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),

]
