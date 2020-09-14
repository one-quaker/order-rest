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
    table = serializers.HyperlinkedRelatedField(
        queryset=Table.objects.all(),
        view_name='order_rest:api-table-detail',
    )
    customer = serializers.HyperlinkedRelatedField(
        queryset=Customer.objects.all(),
        view_name='order_rest:api-customer-detail',
    )

    table_detail = serializers.SerializerMethodField()
    customer_detail = serializers.SerializerMethodField()

    def get_table_detail(self, obj: Order):
        return TableSerializer(obj.table).data

    def get_customer_detail(self, obj: Table):
        return CustomerSerializer(obj.customer).data

    def validate(self, attrs):
        table = attrs['table']
        booking_date = attrs['booking_date']
        if Order.objects.filter(table=table, booking_date=booking_date).exists():
            raise serializers.ValidationError(f'Table number: {table.number} - already booked on {booking_date}')
        return attrs

    class Meta:
        model = Order
        fields = ['customer', 'table', 'table_detail', 'customer_detail', 'booking_date']


class TableOrderSerializer(serializers.ModelSerializer):
    is_booked = serializers.SerializerMethodField()

    def get_is_booked(self, obj):
        return obj.id in self.context['booked_tables']

    class Meta:
        model = Table
        fields = ['pk', 'is_booked']
