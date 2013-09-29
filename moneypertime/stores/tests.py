"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from model_mommy import mommy
from nose.tools import istest

from moneypertime.stores.models import Store


class StoreTest(TestCase):
    @istest
    def retrieves_amount_earned_per_second(self):
        size1 = 2
        size2 = 3
        amount = 200.0
        interval = 20

        store = mommy.make(Store, size1=size1, size2=size2, amount=amount, interval=interval)
        store = Store.objects.get(id=store.id)

        self.assertEqual(store.performance, amount / (interval * size1 * size2))

    @istest
    def has_unicode_defined_by_name(self):
        store = mommy.make(Store)

        self.assertEqual(unicode(store), store.name)
