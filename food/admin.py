from django.contrib import admin
from django.utils.html import format_html
from django.shortcuts import reverse

from .models import Dish, Sale, Subscription, DishCategory, Meal


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    readonly_fields = [
        'id',
        'get_image_preview'
    ]

    list_display = [
        'title',
        'description',
        'get_image_list_preview',
    ]

    list_filter = [
        'categories',
    ]

    def get_image_preview(self, obj):
        if not obj.image:
            return 'выберите картинку'
        return format_html(
            '<img src="{url}" style="max-height: 200px;"/>',
            url=obj.image.url
        )
    get_image_preview.short_description = 'превью'

    def get_image_list_preview(self, obj):
        if not obj.image or not obj.id:
            return 'нет картинки'
        edit_url = reverse('admin:food_dish_change', args=(obj.id,))
        return format_html(
            '<a href="{edit_url}"><img src="{src}" style="max-height: 50px;"/>\
                </a>',
            edit_url=edit_url, src=obj.image.url
        )
    get_image_list_preview.short_description = 'превью'


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'sum',
        'payed_at',
        'user',
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


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'id',
        'title',
    ]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    list_display = [
        'id',
        'title',
        'position'
    ]
