from rest_framework import generics
from datetime import datetime

from .serializers import OrderSerializer, CustomerSerializer, TableSerializer, TableOrderSerializer
from .models import Order, Customer, Table


class CustomerListView(generics.ListCreateAPIView):
    """
    API view to retrieve list of Customer or create new
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete Customer    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class OrderListView(generics.ListCreateAPIView):
    """
    API view to retrieve list of Order or create new
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all().select_related('table', 'customer')


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete Order    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class TableListView(generics.ListCreateAPIView):
    """
    API view to retrieve list of Table or create new
    """
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class TableDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete Table
    """
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class TableOrderView(generics.ListAPIView):
    """
    API view to retrieve reserved Tables by date
    """
    serializer_class = TableOrderSerializer
    queryset = Table.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        booking_date = datetime.strptime(self.kwargs['booking_date'], '%d-%m-%Y')
        context['booked_tables'] = list(Order.objects.filter(booking_date=booking_date).values_list('table_id', flat=True))
        return context
