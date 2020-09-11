from rest_framework import serializers

from order_rest.models import Customer, Order, Table


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['pk', 'number', 'seats_count', 'size_x', 'size_y', 'pos_x', 'pos_y', 'shape']


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer()
    customer = CustomerSerializer()

    def validate(self, attrs):
        table = attrs['table']
        booking_date = attrs['booking_date']
        if Order.objects.filter(table=table, booking_date=booking_date).exists():
            raise serializers.ValidationError(f'Table number: {table.number} - already booked on {booking_date}')
        return attrs

    class Meta:
        model = Order
        fields = ['table', 'customer', 'booking_date']


class TableOrderSerializer(serializers.ModelSerializer):
    is_booked = serializers.SerializerMethodField()

    def get_is_booked(self, obj):
        return obj.id in self.context['booked_tables']

    class Meta:
        model = Table
        fields = ['pk', 'is_booked']
