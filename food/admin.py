from django.contrib import admin

from .models import Dish, DishItem, Product, Sale, Subscription


class DishItemInline(admin.TabularInline):
    model = DishItem


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'title',
        'description',
    ]
    inlines = [DishItemInline]


@admin.register(DishItem)
class DishItemAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'dish',
        'product',
        'quantity',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'title',
        'price',
    ]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'sum',
        'payed_at',
    ]
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'title',
        'duration',
        'price',
    ]
