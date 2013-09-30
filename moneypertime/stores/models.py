from django.db import models


PRICE_TYPE_CHOICES = (
    ('C', 'Cash'),
    ('G', 'Gold'),
)


class Store(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField(help_text='Price of the store itself')
    price_type = models.CharField(choices=PRICE_TYPE_CHOICES, max_length=1, default=PRICE_TYPE_CHOICES[0][0])
    employees = models.IntegerField(help_text='Number of employees accepted initially')
    experience = models.IntegerField(help_text='Experience earned when built')
    size1 = models.SmallIntegerField(help_text='Size of one of the sides of the store')
    size2 = models.SmallIntegerField(help_text='Size the other side of the store')
    build_time = models.IntegerField(help_text='Time spent to build this store')
    should_create_on_water = models.BooleanField(help_text='Should the store be created on water?', default=False)
    amount = models.IntegerField(help_text='Amount earned per interval')
    interval = models.IntegerField(help_text='Interval, in seconds, in which the amount is earned')

    def __unicode__(self):
        return self.name

    @property
    def performance(self):
        return float(self.amount) / (self.interval * self.size1 * self.size2)
