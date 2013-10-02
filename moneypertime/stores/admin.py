import datetime

from django.contrib import admin

from moneypertime.stores.models import Store


def size(instance):
    return u'{}x{}'.format(instance.size1, instance.size2)


def build_time(instance):
    seconds = instance.build_time
    return str(datetime.timedelta(seconds=seconds))
build_time.admin_order_field = 'build_time'


def interval(instance):
    seconds = instance.interval
    return str(datetime.timedelta(seconds=seconds))
interval.admin_order_field = 'interval'


class PerformanceFilter(admin.SimpleListFilter):
    title = 'performance'
    parameter_name = 'performance'

    def lookups(self, request, model_admin):
        return (
            (0.5, 'From 0.5'),
            (1.0, 'From 1.0'),
        )

    def queryset(self, request, queryset):
        value = self.value()

        if value is None:
            return

        return queryset.filter(performance__gte=value)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'performance', 'price', 'price_type', 'employees', size, build_time, 'amount', interval, 'should_create_on_water']
    list_filter = ['price_type', 'should_create_on_water', 'size1', 'size2', PerformanceFilter]


admin.site.register(Store, StoreAdmin)