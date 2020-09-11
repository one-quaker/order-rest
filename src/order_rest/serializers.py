from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Order, Table


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email']


class OrderSerializer(serializers.ModelSerializer):
    table = serializers.HyperlinkedRelatedField(
        queryset=Table.objects.all(),
        view_name='table-detail'
    )
    customer = serializers.HyperlinkedRelatedField(
        queryset=Customer.objects.all(),
        view_name='customer-detail'
    )

    class Meta:
        model = Order
        fields = ['table', 'customer', 'booking_date']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['number', 'seats_count', 'shape']
