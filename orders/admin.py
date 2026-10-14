from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = (
        "food",
        "quantity",
        "price",
        "get_item_total",
    )

    def get_item_total(self, obj):
        return obj.get_total()

    get_item_total.short_description = "Subtotal"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "total_amount",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "phone",
        "address",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "user",
        "total_amount",
        "created_at",
    )

    fieldsets = (
        (
            "Order Information",
            {
                "fields": (
                    "user",
                    "total_amount",
                    "status",
                    "created_at",
                )
            },
        ),
        (
            "Delivery Details",
            {
                "fields": (
                    "address",
                    "phone",
                    "payment_method",
                )
            },
        ),
    )

    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "food",
        "quantity",
        "price",
        "get_item_total",
    )

    search_fields = (
        "food__name",
        "order__user__username",
    )

    def get_item_total(self, obj):
        return obj.get_total()

    get_item_total.short_description = "Subtotal"
