from django.urls import include, path, re_path
from django.conf import settings
from rest_framework import serializers, permissions

from order_rest import views as order_views


urlpatterns = [
    path('table/', order_views.TableListView.as_view(), name='api-table-list'),
    path('table/<int:pk>/', order_views.TableDetailView.as_view(), name='api-table-detail'),
    path('order/', order_views.OrderListView.as_view(), name='api-order-list'),
    path('order/<int:pk>/', order_views.OrderDetailView.as_view(), name='api-order-detail'),
    path('customer/', order_views.CustomerListView.as_view(), name='api-customer-list'),
    path('customer/<int:pk>/', order_views.CustomerDetailView.as_view(), name='api-customer-detail'),

    re_path(r'table-order-date/(?P<booking_date>\d{2}-\d{2}-\d{4})$', order_views.TableOrderView.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
