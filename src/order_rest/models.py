from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True, max_length=256)

    def __str__(self):
        return f'{self.name}, {self.email}'


class Table(models.Model):
    SHAPE_RECTANGULAR = 'rectangular'
    SHAPE_OVAL = 'oval'
    SHAPE_CHOICES = (
        (SHAPE_RECTANGULAR, SHAPE_RECTANGULAR),
        (SHAPE_OVAL, SHAPE_OVAL),
    )

    number = models.PositiveIntegerField('Table number', unique=True)
    seats_count = models.PositiveIntegerField('Number of seats', default=4)
    shape = models.CharField('Shape of the table', choices=SHAPE_CHOICES, max_length=12)

    def __str__(self):
        return f'Table #{self.number}, seats: {self.seats_count}'


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    booking_date = models.DateField()

    class Meta:
        unique_together = [['table', 'customer', 'booking_date']]
