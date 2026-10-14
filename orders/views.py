from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from restaurants.models import Food

from .models import Order, OrderItem


def add_to_cart(request, food_id):
    food = get_object_or_404(
        Food,
        id=food_id,
        is_available=True
    )

    cart = request.session.get("cart", {})

    food_id = str(food.id)

    if food_id in cart:
        cart[food_id] += 1
    else:
        cart[food_id] = 1

    request.session["cart"] = cart
    request.session.modified = True

    messages.success(
        request,
        f"{food.name} added to cart."
    )

    return redirect(
        "restaurant_menu",
        restaurant_id=food.restaurant.id
    )


def cart_view(request):
    cart = request.session.get("cart", {})

    cart_items = []
    total = 0

    for food_id, quantity in cart.items():
        food = get_object_or_404(
            Food,
            id=food_id,
            is_available=True
        )

        item_total = food.price * quantity
        total += item_total

        cart_items.append({
            "food": food,
            "quantity": quantity,
            "item_total": item_total,
        })

    return render(
        request,
        "orders/cart.html",
        {
            "cart_items": cart_items,
            "total": total,
        }
    )


def remove_from_cart(request, food_id):
    cart = request.session.get("cart", {})

    food_id = str(food_id)

    if food_id in cart:
        del cart[food_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def increase_quantity(request, food_id):
    cart = request.session.get("cart", {})

    food_id = str(food_id)

    if food_id in cart:
        cart[food_id] += 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def decrease_quantity(request, food_id):
    cart = request.session.get("cart", {})

    food_id = str(food_id)

    if food_id in cart:
        cart[food_id] -= 1

        if cart[food_id] <= 0:
            del cart[food_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


@login_required
def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart")

    cart_items = []
    total = 0

    for food_id, quantity in cart.items():
        food = get_object_or_404(
            Food,
            id=food_id,
            is_available=True
        )

        item_total = food.price * quantity
        total += item_total

        cart_items.append({
            "food": food,
            "quantity": quantity,
            "item_total": item_total,
        })

    if request.method == "POST":
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        payment_method = request.POST.get("payment_method")

        if not address or not phone or not payment_method:
            messages.error(
                request,
                "Please fill in all checkout details."
            )

            return render(
                request,
                "orders/checkout.html",
                {
                    "cart_items": cart_items,
                    "total": total,
                }
            )

        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            status="pending",
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                food=item["food"],
                quantity=item["quantity"],
                price=item["food"].price,
            )

        request.session["cart"] = {}
        request.session.modified = True

        return redirect(
            "order_success",
            order_id=order.id
        )

    return render(
        request,
        "orders/checkout.html",
        {
            "cart_items": cart_items,
            "total": total,
        }
    )


@login_required
def order_success(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    items = OrderItem.objects.filter(order=order)

    return render(
        request,
        "orders/order_success.html",
        {
            "order": order,
            "items": items,
        }
    )


@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "orders/my_orders.html",
        {
            "orders": orders
        }
    )
