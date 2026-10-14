from django.urls import path

from . import views


urlpatterns = [
    path(
        "add/<int:food_id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
        "",
        views.cart_view,
        name="cart"
    ),

    path(
        "remove/<int:food_id>/",
        views.remove_from_cart,
        name="remove_from_cart"
    ),

    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    path(
        "success/<int:order_id>/",
        views.order_success,
        name="order_success"
    ),
    path(
        "my-orders/",
         views.my_orders,
         name="my_orders"
    ),
    path(
        "increase/<int:food_id>/",
        views.increase_quantity,
        name="increase_quantity"
    ),

    path(
        "decrease/<int:food_id>/",
        views.decrease_quantity,
        name="decrease_quantity"
    ),

]
