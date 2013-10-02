from django.contrib import admin

from moneypertime.stores.models import Store


def size(instance):
    return u'{}x{}'.format(instance.size1, instance.size2)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'performance', 'price', 'price_type', 'employees', size, 'build_time', 'amount', 'interval', 'should_create_on_water']
    list_filter = ['price_type', 'should_create_on_water', 'size1', 'size2']


admin.site.register(Store, StoreAdmin)