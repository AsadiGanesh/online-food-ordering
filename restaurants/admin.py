from django.contrib import admin
from .models import Restaurant, Category, Food


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'is_active')
    search_fields = ('name', 'address')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    list_filter = ('restaurant',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'restaurant',
        'category',
        'price',
        'is_available'
    )

    list_filter = (
        'restaurant',
        'category',
        'is_available'
    )

    search_fields = ('name',)