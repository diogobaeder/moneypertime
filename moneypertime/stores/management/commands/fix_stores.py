import codecs
import json
import os

from django.core.management.base import BaseCommand

from moneypertime.stores.models import Store


class Command(BaseCommand):
    help = 'Fixes stores performances'

    def handle(self, *args, **options):
        stores = Store.objects.all()

        for store in stores:
            store.save()
