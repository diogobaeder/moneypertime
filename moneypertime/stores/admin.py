from django.contrib import admin

from moneypertime.stores.models import Store


def performance(instance):
    return instance.performance


def size(instance):
    return u'{}x{}'.format(instance.size1, instance.size2)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', performance, 'price', 'price_type', 'employees', size, 'build_time', 'amount', 'interval']


admin.site.register(Store, StoreAdmin)