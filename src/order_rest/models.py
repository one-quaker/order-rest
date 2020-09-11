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
    size_x = models.PositiveIntegerField('Size X in %', default=1)
    size_y = models.PositiveIntegerField('Size Y in %', default=2)
    pos_x = models.PositiveIntegerField('Position X', default=0)
    pos_y = models.PositiveIntegerField('Position Y', default=0)
    shape = models.CharField('Shape of the table', choices=SHAPE_CHOICES, max_length=12)

    def __str__(self):
        return f'Table #{self.number}, seats: {self.seats_count}'


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    booking_date = models.DateField()

    class Meta:
        unique_together = [['table', 'customer', 'booking_date']]

    def __str__(self):
        return f'{self.table} | {self.customer} | {self.booking_date}'
